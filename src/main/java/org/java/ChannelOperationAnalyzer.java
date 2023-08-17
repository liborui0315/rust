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

public class ChannelOperationAnalyzer {

    // Counters for channel primitives
    private int sendCount = 0;
    private int recvCount = 0;
    private int tryRecvCount = 0;
    private int dropCount = 0;
    private int iterationRecvCount = 0;

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

        PrimitiveVisitor visitor = new PrimitiveVisitor();
        visitor.visit(tree);
    }

    private class PrimitiveVisitor extends RustParserBaseVisitor<Void> {

        @Override
        public Void visitMethodCallExpression(RustParser.MethodCallExpressionContext ctx) {
            String methodName = ctx.pathExprSegment().getText();
            if ("send".equals(methodName)) {
                sendCount++;
            } else if ("recv".equals(methodName)) {
                recvCount++;
            } else if ("try_recv".equals(methodName)) {
                tryRecvCount++;
            } else if ("drop".equals(methodName)) {
                dropCount++;
            }
            return super.visitMethodCallExpression(ctx);
        }

        @Override
        public Void visitIteratorLoopExpression(RustParser.IteratorLoopExpressionContext ctx) {
            if (ctx.expression().getText().contains("recv")) {
                iterationRecvCount++;
            }
            return super.visitIteratorLoopExpression(ctx);
        }
    }

    private void resetCounters() {
        sendCount = 0;
        recvCount = 0;
        tryRecvCount = 0;
        dropCount = 0;
        iterationRecvCount = 0;
    }

    private void saveToCSV(File file, BufferedWriter writer) throws IOException {
        writer.write(file.getName() + "," + sendCount + "," + recvCount + "," + tryRecvCount + "," + dropCount + "," + iterationRecvCount + "\n");
    }

    public static void main(String[] args) {
        ChannelOperationAnalyzer analyzer = new ChannelOperationAnalyzer();

        File directory = new File("C:\\Users\\17434\\Downloads\\antlr-4.13.0-complete\\META-INF\\maven\\org.antlr\\Test\\20_rust_library");

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("channel_operation_analysis.csv"))) {
            // Write header
            writer.write("Filename, send, recv, try_recv, drop, Iteration over receiving\n");
            analyzeDirectory(directory, analyzer, writer);
        } catch (IOException e) {
            System.err.println("Error writing to CSV file: " + e.getMessage());
        }
    }

    private static void analyzeDirectory(File directory, ChannelOperationAnalyzer analyzer, BufferedWriter writer) throws IOException {
        File[] fileArray = directory.listFiles();
        if (fileArray == null) {
            System.err.println("Error accessing the directory: " + directory.getPath());
            return;
        }

        List<File> files = Arrays.asList(fileArray);
        for (File file : files) {
            if (file.isDirectory()) {
                // Recursively analyze subdirectories
                analyzeDirectory(file, analyzer, writer);
            } else if (file.getName().endsWith(".rs")) {
                analyzer.resetCounters();
                analyzer.analyzeFile(file.toPath());
                analyzer.saveToCSV(file, writer);
            }
        }
    }
}
