use std::process::{Command, Output, Child};
mod metrics;
use metrics::Metrics;

/* 
    Struct: Commands
    Arguments: None
    Return: Self

    Description: This struct contains the commands that the program can run. The commands are as follows:
        - install: optional argument that is true if the user has passed the install command to the program
        - build: optional argument that is true if the user has passed the build command to the program
        - url: optional argument that is true if the user has passed a valid url to the program
        - test: optional argument that is true if the user has passed the test command to the program

    Example: 
        let command = Commands::new();
*/

pub struct Commands {
    pub install: Option<bool>,
    pub build: Option<bool>,
    pub url: Option<String>,
    pub test: Option<bool>,
}

impl Commands {
    /* 
        Function: new
        Arguments: None
        Return: Self

        Description: This function initializes the Commands struct and returns a struct containing the commands that the program can run

        Example: 
            let command = Commands::new();
    */

    pub fn new() -> Self {
        Commands {
            install: None,
            build: None,
            url: None,
            test: None,
        }
    }

    /* 
        Function: install
        Arguments: None
        Return: Child

        Description: This function installs the modules required to run the program

        Example: 
            let command = Commands::new();
            command.install();
    */

    pub fn install(&self) -> Child {
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

    /* 
        Function: build
        Arguments: None
        Return: Output

        Description: This function runs the build script

        Example: 
            let command = Commands::new();
            command.build();
    */

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


    /* 
        Function: test
        Arguments: None
        Return: Output

        Description: This function runs the test suite

        Example: 
            let command = Commands::new();
            command.test();
    */


    pub fn test(&self) {
        Command::new("cargo")
            .arg("test")
            .spawn()
            .expect("failed to test");

    }
}
