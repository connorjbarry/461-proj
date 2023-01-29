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
            .arg("derive")
            .spawn()
            .expect("failed to execute process")
    }

    pub fn build(&self) {
        // build 
        Command::new("cargo")
            .arg("build")
            .spawn()
            .expect("failed to build")
    }

    pub fn url(&self) -> Option<String> {
        self.url.clone()
    }

    pub fn test(&self) -> Option<bool> {
        self.test
    }
}
