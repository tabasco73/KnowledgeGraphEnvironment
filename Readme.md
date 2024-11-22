# KnowledgeGraphEnvironment



## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)

---

## Introduction

Project to easily create knowledge graphs manually or based on pydantic schems. 

## Features

- Knowledge Graph Compiler based on pydantic schemas
- Knowledge Graph Compiler based on standard format for nodes and relationships

## Installation

1. Install graphviz engine:
    ```
    brew install graphviz
    ```
(You may have to configure some paths in between here)

2. Activate virtual environment and install dependencies:
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    ```

## Usage


To manually create knowledge graphs, create a file like domains/manual/opt.py and replace with your data. Then adjust the path in main.py and run:
    ```
    python3 main.py
    ```