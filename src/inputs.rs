use clap::Parser;

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

    pub fn command(&self) -> &str {
        &self.command
    }

}