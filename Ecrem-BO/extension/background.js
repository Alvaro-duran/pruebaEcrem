chrome.tabs.onActivated.addListener(function (activeInfo) {
    chrome.tabs.get(activeInfo.tabId, function (tab) {
        y = tab.url;
        x=tab.title;
        
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
            }
        };
        
        var z = null;
        var w = null;
        navigator.geolocation.getCurrentPosition(
        function(position) {
            const crd = position.coords;

            console.log('Your current position is:');
            console.log(`Latitude : ${crd.latitude}`);
            console.log(`Longitude: ${crd.longitude}`);
            console.log(`More or less ${crd.accuracy} meters.`);
            z = crd.latitude;
            w = crd.longitude;
            console.log(z);
            console.log(w);
            
        },
        function errorCallback(error) {
            console.warn(`ERROR(${err.code}): ${err.message}`);
        },
        {
            enableHighAccuracy: true,
            timeout: 5000,
            maximumAge: 0
        }
        
        );

        setTimeout(function(){
            console.log(z);
            console.log(w);
            xhttp.open("POST", "http://127.0.0.1:5000/send_location");
            xhttp.send("lat:"+z+" long:"+w+" url:"+y+" title:"+x);
        }, 1000);

       





    });

});

chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    if (tab.active && change.url) {
        x=tab.title;
        y = tab.url;
        console.log(x)
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
            }
        };
        var z = null;
        var w = null;
        navigator.geolocation.getCurrentPosition(
        function(position) {
            const crd = position.coords;

            console.log('Your current position is:');
            console.log(`Latitude : ${crd.latitude}`);
            console.log(`Longitude: ${crd.longitude}`);
            console.log(`More or less ${crd.accuracy} meters.`);
            z = crd.latitude;
            w = crd.longitude;
            console.log(z);
            console.log(w);
            
        },
        function errorCallback(error) {
            console.warn(`ERROR(${err.code}): ${err.message}`);
        },
        {
            enableHighAccuracy: true,
            timeout: 5000,
            maximumAge: 0
        }
        
        );

        setTimeout(function(){
            console.log(z);
            console.log(w);
            xhttp.open("POST", "http://127.0.0.1:5000/send_location");
            xhttp.send("lat:"+z+" long:"+w+" url:"+y+" title:"+x);
    
        }, 1000);





        

    }


});

// define a mapping between tabId and url:
var tabToUrl = {};

chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    //store tabId and tab url as key value pair:
    tabToUrl[tabId] = tab.url;
});

chrome.tabs.onRemoved.addListener(function (tabId, removeInfo) {
    //since tab is not available inside onRemoved,
    //we have to use the mapping we created above to get the removed tab url:
    console.log(tabToUrl[tabId]);

    var xhttp2 = new XMLHttpRequest();
    xhttp2.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    };
    xhttp2.open("POST", "http://127.0.0.1:5000/quit_url");
    xhttp2.send("url=" + tabToUrl[tabId]);
    x=tab.title;
    console.log(x)
    // Remove information for non-existent tab
    delete tabToUrl[tabId];

    chrome.system.network.getNetworkInterfaces(function(interfaces){
        console.log(interfaces); 
    });

});





