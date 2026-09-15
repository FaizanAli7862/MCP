import streamlit as st

# Page Configuration

st.set_page_config(
    page_title="MCP Utility Server",
    layout="centered"
)

# Header

st.title("MCP Utility Server")

st.caption(
    "This project demonstrates the Model Context Protocol (MCP), "
    "which allows AI applications to connect with external tools "
    "and use their capabilities in a standardized and reliable way."
)

# st.info(
#     "MCP helps AI systems interact with tools and external resources "
#     "such as calculators, files, databases, APIs, and other services "
#     "without tightly coupling the AI application to each individual tool."
# )

st.divider()

# -----------------------------
# Tool Selection
# -----------------------------
st.subheader("Available MCP Tools")

tool = st.selectbox(
    "Select a tool",
    [
        "Calculator",
        "Text Analyzer",
        "File Reader"
    ]
)

st.divider()

# =========================================================
# Calculator
# =========================================================

if tool == "Calculator":

    st.subheader("Calculator")

    st.write(
        "Use the calculator tool to evaluate mathematical expressions."
    )

    expression = st.text_input(
        "Enter mathematical expression",
        placeholder="Example: 25 * 15 + 100"
    )

    if st.button("Calculate", use_container_width=True):

        if expression.strip():

            try:
                result = eval(
                    expression,
                    {"__builtins__": {}},
                    {}
                )

                st.success(f"Result: {result}")

            except Exception:

                st.error(
                    "Invalid mathematical expression. "
                    "Please enter a valid expression."
                )

        else:

            st.warning(
                "Please enter a mathematical expression."
            )


# =========================================================
# Text Analyzer
# =========================================================

elif tool == "Text Analyzer":

    st.subheader("Text Analyzer")

    st.write(
        "Analyze text and get basic information such as "
        "character, word, and sentence counts."
    )

    text = st.text_area(
        "Enter your text",
        placeholder="Type or paste your text here...",
        height=180
    )

    if st.button("Analyze Text", use_container_width=True):

        if text.strip():

            characters = len(text)
            words = len(text.split())

            sentences = len([
                sentence
                for sentence in text.split(".")
                if sentence.strip()
            ])

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Characters",
                characters
            )

            col2.metric(
                "Words",
                words
            )

            col3.metric(
                "Sentences",
                sentences
            )

        else:

            st.warning(
                "Please enter some text to analyze."
            )


# =========================================================
# File Reader
# =========================================================

else:

    st.subheader("File Reader")

    st.write(
        "Upload a text file and the file reader tool will "
        "extract and display its content."
    )

    uploaded_file = st.file_uploader(
        "Choose a text file",
        type=["txt", "csv", "md", "log"]
    )

    if uploaded_file is not None:

        st.success(
            f"File selected: {uploaded_file.name}"
        )

        if st.button(
            "Read File",
            use_container_width=True
        ):

            try:

                file_content = uploaded_file.read()

                decoded_content = file_content.decode(
                    "utf-8"
                )

                st.subheader("File Content")

                st.text_area(
                    "Content",
                    decoded_content,
                    height=350
                )

            except UnicodeDecodeError:

                st.error(
                    "This file could not be decoded as UTF-8. "
                    "Please upload a UTF-8 encoded text file."
                )

            except Exception as e:

                st.error(
                    f"Unable to read the file: {e}"
                )


# =========================================================
# Project Information
# =========================================================

st.divider()

# st.subheader("About this")

# st.write(
#     """
#     **Model Context Protocol (MCP)** is an open protocol that
#     provides a standardized way for AI applications to connect
#     with external tools and resources.

#     This project demonstrates the concept through three utility
#     capabilities:

#     • **Calculator** — performs mathematical calculations.

#     • **Text Analyzer** — analyzes text and provides basic
#       statistics.

#     • **File Reader** — reads uploaded text-based files and
#       displays their contents.

#     The purpose of this project is to demonstrate how an MCP-based
#     architecture can separate an application's intelligence from
#     the tools it uses, making integrations easier to manage,
#     extend, and maintain.
#     """
# )