mod inputs;
use inputs::Args;

fn main() {
    let args = Args::new();
    Args::parse_commands(&args);
}
