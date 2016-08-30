server {
	listen 80;
	server_name superlists-staging.natanielstrack.com;

	location /static {
		alias /home/ubuntu/sites/superlists-staging.natanielstrack.com/static;
	}

	location / {
		proxy_set_header Host $host;
		proxy_pass http://unix:/tmp/superlists-staging.natanielstrack.com.socket;
	}
}
