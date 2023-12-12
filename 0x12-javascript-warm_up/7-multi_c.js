#!/usr/bin/node
if (process.argv.length < 3) {
   console.log('missing number of occurances');
} else  {
	const x = parseInt(process.argv[2]);

	if (isNaN(x)) {
	   console.log('missing number of occurances');
} else {
   let i = 0;
  while (i < x) {
     console.log('C is fun');
     i++;
    } 
  }
}
