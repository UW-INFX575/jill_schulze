# Script to generate URL for an example file from my output

from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection() # Establish S3 connection
my_bucket = conn.get_bucket('jillschulze') # Bucket

key = my_bucket.new_key('PS2/uni_summary.csv') # Path to example output file
example_file_key = my_bucket.get_key(key) # Get key for example file
example_file_key.set_canned_acl('private') # ACL is already set to private, so this has no effect

print example_file_key.generate_url(604800, query_auth=True) # Generate URL that will last for 7 days
