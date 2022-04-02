"use-strict";

/*
250
1/3/2012 16:00:00   Missing_1
1/4/2012 16:00:00   27.47
1/5/2012 16:00:00   27.728
1/6/2012 16:00:00   28.19
1/9/2012 16:00:00   28.1
1/10/2012 16:00:00  28.15
12/13/2012 16:00:00 27.52
12/14/2012 16:00:00 Missing_19
12/17/2012 16:00:00 27.215
12/18/2012 16:00:00 27.63
12/19/2012 16:00:00 27.73
12/20/2012 16:00:00 Missing_20
12/21/2012 16:00:00 27.49
12/24/2012 13:00:00 27.25
12/26/2012 16:00:00 27.2
12/27/2012 16:00:00 27.09
12/28/2012 16:00:00 26.9
12/31/2012 16:00:00 26.77
*/

data = [
    "1/3/2012 16:00:00\tMissing_1",
    "1/4/2012 16:00:00\t27.47",
    "1/5/2012 16:00:00\t27.728",
    "1/6/2012 16:00:00\t28.19",
    "1/9/2012 16:00:00\t28.1",
    "1/10/2012 16:00:00\t28.15",
    "12/13/2012 16:00:00\t27.52",
    "12/14/2012 16:00:00\tMissing_19",
    "12/17/2012 16:00:00\t27.215",
    "12/18/2012 16:00:00\t27.63",
    "12/19/2012 16:00:00\t27.73",
    "12/20/2012 16:00:00\tMissing_20",
    "12/21/2012 16:00:00\t27.49",
    "12/24/2012 13:00:00\t27.25",
    "12/26/2012 16:00:00\t27.2",
    "12/27/2012 16:00:00\t27.09",
    "12/28/2012 16:00:00\t26.9",
    "12/31/2012 16:00:00\t26.77",
    "1/3/2012 16:00:00\tMissing_111"
]

function parseData(readings) {
    let data = [];
    for (let i = 0; i < readings.length; i++) {
        let r = readings[i].split("\t");
        data.push([Date.parse(r[0]), r[1].match(/Missing/) ? NaN : Number(r[1])]);
    }
    return data;
}

function interpolateValue(data, min, max) {
    let sample = data.slice(min,max);
    //console.log("sample", sample)
    sample = sample.filter(e => { return !isNaN(e[1]) });
    //console.log("filtered-sample", sample)
    let sum = sample.reduce((acc, e) => acc + e[1], 0);
    let avg = (sum / sample.length) || 0;
    return avg.toFixed(2);
}

function calcMissing(readings) {
    // Write your code here
    const WINDOW = 2;
    let data = parseData(readings);
    data.sort((a,b) => { return a[0] - b[0] }) // order data by timestamp, because we never know...
    for (let i = 0; i < data.length; i++) {
        if (isNaN(data[i][1])) { // found missing day
            if (i == 0) { // there is no day before, so only look for the closest next day after
                console.log(interpolateValue(data, i, i + WINDOW + 1) );
            } 
            else if (i == data.length - 1) { // there is no day after, so look for the closest day before
                console.log(interpolateValue(data, i - WINDOW, i) );
            } 
            else {
                let min = i - WINDOW < 0 ? 0 : i - WINDOW; 
                let max = i + WINDOW > data.length - 1 ? data.length - 1 : i + WINDOW; 
                console.log(interpolateValue(data, min, max) );
            }
        }
    }
}

// calcMissing(data);

// ###############################################################################################################################################################################

// https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=pizza

const https = require("https")

count_topic_words = async (topic) => {
    
    return new Promise((resolve, reject) => {

        const options = {
            host: "en.wikipedia.org",
            path: `/w/api.php?action=parse&format=json&page=${topic}`,
            method: 'GET'
        }
    
        var data = ''
    
        https.request(options, (response) => {
    
            response.on('data', function (chunk) {
                data += chunk;
            });
    
            response.on('end', () => {
                data = JSON.parse(data);
                // handle data
                let re = new RegExp(`${topic}`, "gi");
                const textTopic = data.parse.text['*'];
                resolve( textTopic.match(re).length );
            });
        })
        .on('error', err => { console.log('Error: ', err.message) })
        .end()
    });

}

(async() => { console.log( await count_topic_words("pizza") ) })();

// ###############################################################################################################################################################################

/*
package com.hackerrank.sample.controller;

import com.hackerrank.sample.dto.StringResponse;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SampleController {

  @RequestMapping(value = "/defaultHello", method = RequestMethod.GET)
  ResponseEntity<StringResponse> defaultHello() {
    StringResponse sr = new StringResponse("Default Hello World!");
    return ResponseEntity.status(HttpStatus.OK).body(sr);
  }

  @RequestMapping(value = "/customHello", method = RequestMethod.POST)
  public ResponseEntity<StringResponse> customHello(@RequestParam("message") String message) {

    if(message == null) {
      return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(null);
    }

    StringResponse sr = new StringResponse("Custom " + message);
    return ResponseEntity.status(HttpStatus.OK).body(sr);
  }

}
*/