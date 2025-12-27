Thanks for downloading this template!

Template Name: Arsha
Template URL: https://bootstrapmade.com/arsha-free-bootstrap-html-template-corporate/
Author: BootstrapMade.com
License: https://bootstrapmade.com/license/



## Nginx config



## SSL
opencert command:

```
certbot certonly --nginx --standalone --preferred-challenges http --agree-tos --email ruzbeh@gmail.com -d futurestrategy.space
```


## Nginx config

```
# cat future_strategy_space.conf 

server {

      # The host name to respond to
      server_name futurestrategy.space
        
      index index.html;
      root /var/www/html/future_strategy_space;

    
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/futurestrategy.space/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/futurestrategy.space/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

server {
    if ($host = futurestrategy.space) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


      listen 80;
        server_name futurestrategy.space
        
      index index.html;
    return 404; # managed by Certbot


}
```