## Readme File

To run the code first execute following commands in terminal
1.	ulimit -Sn 10000
	This will set number of open files to 10000, it is necessary since we need to read almost 3000 files located in 'enron/' directory.

2.	alias enron_search='python3 code.py'
	Then this will create an alias for command 'python3 code.py' as 'enron_search'

After this the code can be executed by running command 
	'enron_search term_search hide all the evidence'
	'enron_search address_search Gus Perez'
	'enron_search interaction_search ina.rangel@enron.com information.management@enron.com'

Wait patiently for each of this output.