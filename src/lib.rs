#[cfg(test)]


mod tests {
    use std::process::Command;
    #[test]
    fn url_parsing() {
        let file1 = "sample/test_url/testurl_1.txt";
        let file2 = "sample/test_url/testurl_2.txt";

        // call python script to parse the url
        Command::new("python3")
            .arg("src/valid_url.py")
            .arg(file1)
            .arg("output1.txt")
            .spawn()
            .expect("failed to execute process");

        Command::new("python3")
            .arg("src/valid_url.py")
            .arg(file2)
            .arg("output2.txt")
            .spawn()
            .expect("failed to execute process");

        // check if the output is correct from sample/test_url/resulturl files
        let mut result1 = "sample/test_url/resulturl_1.txt";
        let mut result2 = "sample/test_url/resulturl_2.txt";

        // replace results /r/n with /n
        let mut contents = std::fs::read_to_string(result1).unwrap();
        contents = contents.replace("\r\n", "\n");
        std::fs::write(result1, contents).unwrap();
        contents = std::fs::read_to_string(result2).unwrap();
        contents = contents.replace("\r\n", "\n");
        std::fs::write(result2, contents).unwrap();

        // compare the output of the python script with the result files
        assert_eq!(std::fs::read_to_string("output1.txt").unwrap(), std::fs::read_to_string(result1).unwrap());
        assert_eq!(std::fs::read_to_string("output2.txt").unwrap(), std::fs::read_to_string(result2).unwrap());
    }

}
