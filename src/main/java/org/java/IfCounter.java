package org.java;

import org.antlr.v4.runtime.*;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.HashMap;
import java.util.Map;

public class IfCounter {

    public static void main(String[] args) throws IOException {
        URL resourceURL = IfCounter.class.getClassLoader().getResource("");
        File folder = new File(resourceURL.getPath());
        File[] listOfFiles = folder.listFiles();

        Map<String, Integer> fileIfCounts = new HashMap<>();

        for (File file : listOfFiles) {
            if (file.isFile() && file.getName().endsWith(".rs")) {
                try {
                    CharStream charStream = CharStreams.fromFileName(file.getAbsolutePath());
                    RustLexer lexer = new RustLexer(charStream);
                    CommonTokenStream tokens = new CommonTokenStream(lexer);
                    tokens.fill();

                    int ifCount = (int) tokens.getTokens().stream().filter(t -> t.getType() == RustLexer.KW_IF).count();
                    fileIfCounts.put(file.getName(), ifCount);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        // Print results
        // Define the path for the CSV file
        Path csvOutputPath = Paths.get("if_counts.csv");

        // Write the header to the CSV file
        Files.write(csvOutputPath, "File,If Count\n".getBytes(StandardCharsets.UTF_8));

        // Write the results to the CSV file
        for (Map.Entry<String, Integer> entry : fileIfCounts.entrySet()) {
            String line = entry.getKey() + "," + entry.getValue() + "\n";
            Files.write(csvOutputPath, line.getBytes(StandardCharsets.UTF_8), StandardOpenOption.APPEND);
        }
    }
}

