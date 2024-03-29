package org.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@CrossOrigin
@EnableAutoConfiguration
public class MyApplication {
    @RequestMapping("/")
    String home() {
        return "Hello World1111!";
    }
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}