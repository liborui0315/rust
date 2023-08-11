package org.java;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

import java.io.IOException;
import java.io.InputStream;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.HashMap;
import java.util.Map;


public class Main {

    public static class IfCountingListener extends RustParserBaseListener {
        private int ifCount = 0;

        @Override
        public void enterIfExpression(RustParser.IfExpressionContext ctx) {
            ifCount++;
        }

        public int getIfCount() {
            return ifCount;
        }
    }



    public static void main(String[] args) throws URISyntaxException, IOException {
        System.out.println("Hello world!");

        // use listener to walk the ast
        // count the number of if statements in the given examples and output as csv

//        Path examplesPath = Paths.get("C:/Users/17434/Downloads/antlr-4.13.0-complete/META-INF/maven/org.antlr/Test/examples");


//        try {
//            InputStream inputStream = Main.class.getResourceAsStream("/v1_48_0_unsafe_mod.rs");
//            RustLexer rustLexer = new RustLexer(CharStreams.fromStream(inputStream));
//
//            TokenStream tokenStream = new CommonTokenStream(rustLexer);
//            RustParser rustParser = new RustParser(tokenStream);
//            rustParser.crate();
//
//
//        } catch (IOException e) {
//            e.printStackTrace();
//        }

        // Assuming resources is the root classpath directory
        URL url = Main.class.getResource("/");
        Path resourcesPath = Paths.get(url.toURI());

        try (DirectoryStream<Path> directoryStream = Files.newDirectoryStream(resourcesPath)) {
            for (Path file : directoryStream) {
                // Make sure it's a file, not a subdirectory
                if (Files.isRegularFile(file)) {
                    InputStream inputStream = Files.newInputStream(file);
                    RustLexer rustLexer = new RustLexer(CharStreams.fromStream(inputStream));

                    TokenStream tokenStream = new CommonTokenStream(rustLexer);
                    RustParser rustParser = new RustParser(tokenStream);

//                    rustParser.removeErrorListeners();
//                    rustParser.addErrorListener(new BaseErrorListener() {
//                        @Override
//                        public void syntaxError(Recognizer<?, ?> recognizer, Object offendingSymbol, int line, int charPositionInLine, String msg, RecognitionException e) {
//                            throw new IllegalStateException("Failed to parse at line " + line + " position " + charPositionInLine + ": " + msg, e);
//                        }
//                    });
                    rustParser.crate();

                    inputStream.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Call the main method of IfCounter class
//        IfCounter.main(args);



/*
* The following code segment is used to test which file produces an error during parsing.
*/


        String[] fileNames = {
                "/comment.rs", "/deno_core_runtime.rs", "/hello.rs",
                "/inlinepython_example.rs", "/intellijrust_test_allinone.rs",
                "/issue_1985_raw_string.rs", "/leaf_vmessstream.rs", "/literal.rs",
                "/rustls_quic.rs", "/ssrust_config.rs", "/ssrust_ssserver.rs",
                "/v1_46_0_split_float_literal.rs", "/v1_46_0_split_float_literal.rs.tree",
                "/v1_48_0_unsafe_mod.rs", "/v1_53_0_or_pattern.rs",
                "/v1_53_0_unicode_identifier.rs", "/v1_56_0_open_range.rs"
        };

        Map<String, Integer> results = new HashMap<>();

        for (String file : fileNames) {
            System.out.println("Parsing " + file + " ...");
            try {
                InputStream inputStream = Main.class.getResourceAsStream(file);
                RustLexer rustLexer = new RustLexer(CharStreams.fromStream(inputStream));

                TokenStream tokenStream = new CommonTokenStream(rustLexer);
                RustParser rustParser = new RustParser(tokenStream);

                ParseTree parseTree = rustParser.crate();

                rustParser.crate();
                IfCountingListener listener = new IfCountingListener();
                ParseTreeWalker.DEFAULT.walk(listener, parseTree);

                results.put(file, listener.getIfCount());

                System.out.println("Successfully parsed " + file);
            } catch (Exception e) {
                System.err.println("Failed to parse " + file);
                e.printStackTrace();
            }
        }

        // Write the results to a CSV file
        Path outputPath = Paths.get("if_counts.csv");
        try {
            Files.write(outputPath, "File,If Count\n".getBytes(StandardCharsets.UTF_8));
            // Loop through fileNames array instead of the map
            for (String fileName : fileNames) {
                String line = fileName + "," + results.getOrDefault(fileName, 0) + "\n";
                Files.write(outputPath, line.getBytes(StandardCharsets.UTF_8), StandardOpenOption.APPEND);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }



    }


}




