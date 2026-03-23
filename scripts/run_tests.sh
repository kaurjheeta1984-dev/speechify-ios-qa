#!/bin/bash
# run_tests.sh — Convenience script to run the test suite locally
# Usage: bash scripts/run_tests.sh [option]
#   Options: smoke | functional | regression | edge | all (default: all)

set -e  # Exit on any error

REPORT_DIR="reports"
mkdir -p "$REPORT_DIR"

SUITE=${1:-all}

echo "============================================"
echo "  Speechify iOS QA Automation"
echo "  Running suite: $SUITE"
echo "============================================"

case "$SUITE" in
  smoke)
    echo "▶ Running SMOKE tests (P0 only)..."
    pytest tests/ -m "smoke" -v \
      --html="$REPORT_DIR/smoke_report.html" \
      --self-contained-html
    ;;
  functional)
    echo "▶ Running FUNCTIONAL tests..."
    pytest tests/functional/ -v \
      --html="$REPORT_DIR/functional_report.html" \
      --self-contained-html
    ;;
  regression)
    echo "▶ Running REGRESSION suite..."
    pytest tests/regression/ -v \
      --html="$REPORT_DIR/regression_report.html" \
      --self-contained-html
    ;;
  edge)
    echo "▶ Running EDGE CASE tests..."
    pytest tests/edge_cases/ -v \
      --html="$REPORT_DIR/edge_report.html" \
      --self-contained-html
    ;;
  all)
    echo "▶ Running ALL tests..."
    pytest tests/ -v \
      --html="$REPORT_DIR/full_report.html" \
      --self-contained-html \
      --tb=short
    ;;
  *)
    echo "Unknown suite: $SUITE"
    echo "Usage: bash scripts/run_tests.sh [smoke|functional|regression|edge|all]"
    exit 1
    ;;
esac

echo ""
echo "✅ Done! Open $REPORT_DIR/ to view the HTML report."
