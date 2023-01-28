use std::process::{Command, Output};

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

    pub fn install(&self) -> Vec<u8> {
        let output: Output = Command::new("ls")
            .args(["-l", "-a"])
            .output()
            .expect("failed to execute process");

        println!("here {} ", output.status);
        output.stdout
    }

    pub fn build(&self) -> Option<bool> {
        self.build
    }

    pub fn url(&self) -> Option<String> {
        self.url.clone()
    }

    pub fn test(&self) -> Option<bool> {
        self.test
    }
}