use clap::Parser;
pub mod commands;
use commands::Commands;


/* 
    Struct to parse the arguments passed to the program using clap
    This struct uses the clap syntax found at https://docs.rs/clap/latest/clap/
*/

#[derive(Parser, Debug)]
#[command(author,version,about,long_about=None)]
pub struct Args {
    /// The command to execute
    #[arg(short, long)]
    pub command: String,
}

impl Args {
    /* 
        Function: new
        Arguments: None
        Return: Self

        Description: This function parses the arguments passed to the program using clap and returns a struct containing the arguments passed to the program

        Example: 
            let args = Args::new();
    */
    
    pub fn new() -> Self {
        Args::parse()
    }


    /* 
        Function: parse_commands
        Arguments: None  - requires the struct to be initialized
        Return: None

        Description: This function parses the commands passed to the program and runs the appropriate command
            - install: installs the modules required to run the program
            - build: runs the build script
            - test: runs the test suite
            - _: checks to see if the url passed to the program is a valid url and if it is, it grades the module and returns the grade to the user. If the url is not valid, it calls the {invalid args} function and returns an error message to the user

        Example: 
            let args = Args::new();
            args.parse_commands();
    */

    pub fn parse_commands(&self) {
        let mut command = Commands::new();
        match self.command.as_str() {
            "install" => {
                println!("This has entered the install parser");
                command.install = Some(true);
                command.install();
            },
            "build" => println!("{}", self.command), 
            "test" => println!("{}", self.command),
            _ => println!("{}", self.command),
        }
    }
}