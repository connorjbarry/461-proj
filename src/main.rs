mod inputs;
use inputs::Args;

fn main() {
    let args = Args::new();
    println!("{}", args.command());
}
