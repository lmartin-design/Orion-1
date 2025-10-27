# Orion-1

## Introduction

Orion-1 is a lightweight Markov-chain based AI model designed to generate text without a separate training phase. Instead of training in the conventional sense, Orion-1 compiles input data into a compact model representation. Without optional JSON storage, the core implementation is intentionally small and easy to inspect.

## Why use Orion-1?

Orion-1 is useful when you need a fast, memory-efficient generator that can produce plausible sequences from example data with minimal setup. It is well suited for prototyping, embedding into small tools, or educational purposes where transparency and simplicity matter more than state-of-the-art language quality.

## Features

- No heavy training required — compile example data into the model.
- Very small codebase and fast startup.
- Optional JSON-based storage for persisting compiled models.
- Easy to read and modify — designed for developers and learners.

## Quick Start

1. Prepare a corpus of example text (plain text files or a simple JSON format).
2. Run the provided compiler/loader to build the Markov model from your corpus.
3. Use the generator API to produce sequences using the compiled model.

## Pros and Cons

Pros
- No separate training step required.
- Fast and memory-efficient.
- Simple implementation — easy to understand and extend.

Cons
- Output quality is limited compared to modern neural language models.
- Depends heavily on the quality and quantity of input examples.
- Not suitable for tasks requiring deep semantic understanding or factual accuracy.

## Contributing

Contributions, bug reports, and feature requests are welcome. Please open issues or pull requests with clear descriptions and examples.

## License

GNU GENERAL PUBLIC LICENSE v3.0