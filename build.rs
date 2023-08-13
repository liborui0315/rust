use std::convert::TryInto;
use std::env;
use std::env::VarError;
use std::error::Error;
use std::fs::{read_dir, DirEntry, File};
use std::io::Write;
use std::path::Path;
use std::process::Command;

fn main() {
    let grammars = vec![
        "CSV",
        "ReferenceToATN",
        "XMLLexer",
        "SimpleLR",
        "Labels",
        "FHIRPath",
    ];
    let additional_args = vec![Some("-visitor"), None, None, None, None];
    let antlr_path = "C:\Users\17434\Downloads\antlr-4.11.1-complete.jar";

    for (grammar, arg) in grammars.into_iter().zip(additional_args) {
        //ignoring error because we do not need to run anything when deploying to crates.io
        let _ = gen_for_grammar(grammar, antlr_path, arg);
    }

    println!("cargo:rerun-if-changed=build.rs");

    println!("cargo:rerun-if-changed=C:\Users\17434\Downloads\antlr-4.11.1-complete.jar");
}

fn gen_for_grammar(
    grammar_file_name: &str,
    antlr_path: &str,
    additional_arg: Option<&str>,
) -> Result<(), Box<Error>> {
    // let out_dir = env::var("OUT_DIR").unwrap();
    // let dest_path = Path::new(&out_dir);

    let input = env::current_dir().unwrap().join("grammars");
    let file_name = grammar_file_name.to_owned() + ".g4";

    let c = Command::new("java")
        .current_dir(input)
        .arg("-cp")
        .arg(antlr_path)
        .arg("org.antlr.v4.Tool")
        .arg("-Dlanguage=Rust")
        .arg("-o")
        .arg("../tests/gen")
        .arg(&file_name)
        .args(additional_arg)
        .spawn()
        .expect("antlr tool failed to start")
        .wait_with_output()?;
    // .unwrap()
    // .stdout;
    // eprintln!("xx{}",String::from_utf8(x).unwrap());

    println!("cargo:rerun-if-changed=grammars/{}", file_name);
    Ok(())
}
