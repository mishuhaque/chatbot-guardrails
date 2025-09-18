from setuptools import setup, find_packages

setup(
    name="chatbot-guardrails",
    version="0.1.0",
    description="A plugin to improve chatbot responses by reducing hallucinations and adding fact-checking guardrails.",
    author="Mishu Haque",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "openai",
        "sentence-transformers",
        "faiss-cpu",
        "requests",
    ],
    python_requires=">=3.8",
)
