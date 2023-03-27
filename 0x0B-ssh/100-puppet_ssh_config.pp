# Ensure the SSH client configuration file exists and has the correct content
file { '/home/<your-username>/.ssh/config':
  ensure  => file,              # Create the file if it doesn't exist
  mode    => '0600',            # Set the correct permissions
  content => "Host your_server_hostname\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no\n",  # Set the file content
}

# Add a line to disable password authentication
file_line { 'Turn off passwd auth':
  path => '/home/<your-username>/.ssh/config',  # Specify the path of the file to modify
  line => 'PasswordAuthentication no',          # Set the line to add
}

# Add a line to declare the identity file
file_line { 'Declare identity file':
  path => '/home/<your-username>/.ssh/config',  # Specify the path of the file to modify
  line => 'IdentityFile ~/.ssh/school',         # Set the line to add
}
