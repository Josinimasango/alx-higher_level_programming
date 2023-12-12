#!/usr/bin/node

// check the number of arguments
let argv = arguments.length;

if (process.argv.length === 2){
     //No arguments
     console.log('No argument');
} else if (process.argv.length === 3){
     //Argument found	
console.log('Argument found');
} else {
    // more than 1 argument found	
console.log('Arguments found');
}
