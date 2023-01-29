use clap::Parser;
pub mod commands;
use commands::Commands;

#[derive(Parser, Debug)]
#[command(author,version,about,long_about=None)]
pub struct Args {
    /// The command to execute
    #[arg(short, long)]
    command: String,
}

impl Args {
    pub fn new() -> Self {
        Args::parse()
    }

    pub fn parse_commands(&self) {
        let mut command = Commands::new();
        match self.command.as_str() {
            "install" => {
                println!("This has entered the install parser");
                command.install = Some(true);
                command.install();
            }, // install the modules
            "build" => println!("{}", self.command), // run the build script
            "test" => println!("{}", self.command), // run the test suite
            _ => println!("{}", self.command), //run a check to see if this is the url of a module
        }
    }

}