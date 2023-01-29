mod inputs;
use inputs::Args;
use inputs::commands::Commands;
use std::env;

fn main() {
    let initial_args: Vec<String> = env::args().collect();
    if initial_args.len() < 2 {
        println!("Not enough arguments were passed"); // print an error message to console
    }
    else if initial_args.len() == 3 && initial_args[2] == "install" {
        println!("This is the install command");
        let mut command = Commands::new();
        command.install = Some(true);
        command.install();
    } 
    else {
        let args = Args::new();
        args.parse_commands();
    }
    
}
