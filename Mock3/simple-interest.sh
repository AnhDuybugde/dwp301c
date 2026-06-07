#!/bin/bash

echo "Simple Interest Calculator"
echo "--------------------------"

read -p "Enter the principal amount: " principal
read -p "Enter the rate of interest: " rate
read -p "Enter the time period in years: " time

simple_interest=$(awk "BEGIN {printf \"%.2f\", ($principal * $rate * $time) / 100}")

echo "Principal amount: $principal"
echo "Rate of interest: $rate%"
echo "Time period: $time years"
echo "Simple interest: $simple_interest"
