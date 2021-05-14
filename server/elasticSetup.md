- install elasticsearch
```bash
    curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

    echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list

    sudo apt update

    sudo apt install elasticsearch
```
- config max memory 
``` bash
    sudo nano /etc/elasticsearch/jvm.options
```

``` 
    # Xms represents the initial size of total heap space
    # Xmx represents the maximum size of total heap space

    -Xms1g (uncomment and edit here "Xms<memory size>g" 3 to 4 should be fine) 
    -Xmx1g (uncomment and edit here "Xms<memory size>g" 3 to 4 should be fine)

    # the settings shipped with ES 5 were: -Xms2g
    # the settings shipped with ES 5 were: -Xmx2g
```