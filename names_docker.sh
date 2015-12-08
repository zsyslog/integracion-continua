#!/bin/bash
docker ps -a | perl -ne 'chomp; @cols = split /\s{2,}/, $_; $name=pop @cols; printf "%-28s %-20s %-20s %-30s\n", $name, $cols[1], $cols[3], $cols[4]' | grep -v NAMES | awk '{print $1}'
