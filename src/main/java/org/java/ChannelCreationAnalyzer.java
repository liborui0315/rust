package org.java;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class ChannelCreationAnalyzer {

    // Counter for channel creations
    private int boundedCount = 0;
    private int unboundedCount = 0;

    public void analyzeFile(Path filePath) {
        try {
            String fileContent = Files.readString(filePath);
            analyzeContent(fileContent);
        } catch (IOException e) {
            System.err.println("Error reading file: " + filePath);
            e.printStackTrace();
        }
    }

    private void analyzeContent(String content) {
        CharStream charStream = CharStreams.fromString(content);
        RustLexer lexer = new RustLexer(charStream);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        RustParser parser = new RustParser(tokens);
        ParseTree tree = parser.crate();

        ChannelVisitor visitor = new ChannelVisitor();
        visitor.visit(tree);
    }

    private class ChannelVisitor extends RustParserBaseVisitor<Void> {

        @Override
        public Void visitMethodCallExpression(RustParser.MethodCallExpressionContext ctx) {
            String methodName = ctx.pathExprSegment().getText();
            if ("bounded".equals(methodName)) {
                boundedCount++;
            } else if ("unbounded".equals(methodName)) {
                unboundedCount++;
            }
            return super.visitMethodCallExpression(ctx);
        }
    }

    private void resetCounters() {
        boundedCount = 0;
        unboundedCount = 0;
    }

    private void saveToCSV(File file, BufferedWriter writer) throws IOException {
        writer.write(file.getName() + "," + boundedCount + "," + unboundedCount + "\n");
    }

    public static void main(String[] args) {
        ChannelCreationAnalyzer analyzer = new ChannelCreationAnalyzer();

        File directory = new File("C:\\Users\\17434\\Downloads\\antlr-4.13.0-complete\\META-INF\\maven\\org.antlr\\Test\\20_rust_library");

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("channel_creation_analysis.csv"))) {
            writer.write("Filename, Channel Creation (bounded), Channel Creation (unbounded)\n");  // Write header
            analyzeDirectory(directory, analyzer, writer);
        } catch (IOException e) {
            System.err.println("Error writing to CSV file: " + e.getMessage());
        }
    }

    private static void analyzeDirectory(File directory, ChannelCreationAnalyzer analyzer, BufferedWriter writer) throws IOException {
        File[] fileArray = directory.listFiles();
        if (fileArray == null) {
            System.err.println("Error accessing the directory: " + directory.getPath());
            return;
        }

        List<File> files = Arrays.asList(fileArray);
        for (File file : files) {
            if (file.isDirectory()) {
                analyzeDirectory(file, analyzer, writer);  // Recursively analyze subdirectories
            } else if (file.getName().endsWith(".rs")) {
                analyzer.resetCounters();
                analyzer.analyzeFile(file.toPath());
                analyzer.saveToCSV(file, writer);
            }
        }
    }
}
