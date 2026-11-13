<img width="2172" height="724" alt="Spielstream Real-Time Tech Banner" src="https://github.com/user-attachments/assets/a461a896-b078-439d-8722-de869090beb4" />

# Spielstream

*A local, open-source playground for learning and sharing Streamhouse architectures.*
("Spiel" is German for "play".)

Spielstream is a collection of small, runnable examples that show how a Streamhouse
architecture keeps the current state of a business continuously available to
applications, AI agents and analytics. Everything runs on a laptop with open-source
components:

| Stage | Component |
|---|---|
| Capture | PostgreSQL + Debezium |
| Transport | Redpanda |
| Transform | Apache Flink (SQL) |
| Govern | Redpanda schema registry |
| Serve | PostgreSQL, one FastMCP server for agents, Apache Iceberg on MinIO + DuckDB for history |
| Agents | Ollama with a Python worker |

The first example is the **Fridge Rescue Squad**: when food in the fridge is about to
expire, an AI agent proposes a dish to rescue it, using whatever is actually in the fridge.

## Status

Early planning. This `0.0.1` release only provides a small command-line tool:

```
pip install spielstream
spielstream info
spielstream --version
```

The platform, examples and tutorials are being built in the repository:
https://github.com/spielstream/spielstream

## Contributing

Spielstream is designed so the community can add its own examples. Contribution
guidelines will be published in the repository before the first public release.

## A note on the name "Streamhouse"

"Streamhouse" is used here only as a category descriptor, in line with the public
Streamhouse Trademark Commitment. Spielstream is an independent community project and
is not affiliated with, endorsed or certified by the Streamhouse Working Group.

## License

Apache License 2.0. See `LICENSE`.
