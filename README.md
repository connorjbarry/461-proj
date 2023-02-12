# Overview

Project step 1 for Purdue ECE 30861 - Software Engineering

Team Members:\
Yi-Hsiang (Sean) Chang\
Connor Barry\
Erik Hays\
Seth Karner

## Project Description

This application is based upon a real-world scenario, prompted to us in ECE 30861 - Software Engineering at Purdue University. The task requires us to act as subcontractors for the ACME Corporation, recently one of their back-end components were ported to Node.js. Based upon success of this service, they want to bring up new Node.js-based services. As the team that provides infrastructure for the ACME Corp. we are tasked with making it easier for the services teams to get up and running.

## Service Description

The service will be prompted with a list of npm modules to grade. The service will then grade each module and return the results to the user in tabular format in the console. The grading will be based upon the following criteria:

- Ramp-up Time
- Correctness
- Bus Factor
- Responsiveness
- License Compatibility

These criteria will be graded on a scale of 0-1 with 1 being the best score. The total score will be calculated by an equation determined from the importance of each metric to the ACME Corpm and seen below:

## Getting Started

The command line interface supports the following commands:

- `install` - Installs the necessary dependencies for the application to function
- `build` - Builds the application and services. This is required before running the application
- `test` - Runs the test suite
- `url-file` - This is the path to a file containing a list of URLs to grade (one per line)

### To run these commands, input the following into the command line

```bash
./run <command>
```
