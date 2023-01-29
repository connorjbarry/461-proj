use std::process::{Command, Output, Child};
mod metrics;
use metrics::Metrics;

pub struct Commands {
    pub install: Option<bool>,
    pub build: Option<bool>,
    pub url: Option<String>,
    pub test: Option<bool>,
}

impl Commands {
    pub fn new() -> Self {
        Commands {
            install: None,
            build: None,
            url: None,
            test: None,
        }
    }

    pub fn install(&self) -> Child {
        // let output: Output = Command::new("ls")
        //     .arg("-a")
        //     .arg("-l")
        //     .spawn()
        //     .expect("failed to execute process");

        // println!("here {} ", output.status);
        // output.stdout
        Command::new("cargo")
            .arg("add")
            .arg("clap")
            .arg("--features")
            .arg("clap/derive")
            .arg("reqwest")
            .arg("serde")
            .arg("serde_json")
            .arg("serde_derive")
            .spawn()
            .expect("failed to execute process")
    }

    pub fn build(&self) -> Option<bool> { //cargo build
        self.build
    }

    pub fn url(&self) -> Option<String> {
        self.url.clone()
    }

    pub fn test(&self) -> Option<bool> { //cargo test
        self.test
    }
    pub fn invalidCommand(&self) -> Option<bool> {
        None
    }
}