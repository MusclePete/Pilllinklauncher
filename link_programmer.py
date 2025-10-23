import gradio as gr
import os
import tempfile

def escape_js_string(s):
    """Escape special characters for JavaScript string literals."""
    return s.replace('"', '\\"').replace('\n', '\\n')

def generate_html(button1_label, button1_url, button2_label, button2_url, button3_label, button3_url,
                 button4_label, button4_url, button5_label, button5_url, button6_label, button6_url,
                 button7_label, button7_url, button8_label, button8_url, button9_label, button9_url,
                 button10_label, button10_url, filename):
    # Default links and labels
    default_links = [
        {"url": "localhost:7860", "label": "LH7860"},
        {"url": "https://www.google.com", "label": "Google"},
        {"url": "https://www.github.com", "label": "GitHub"},
        {"url": "https://www.stackoverflow.com", "label": "Stack Overflow"},
        {"url": "https://www.wikipedia.org", "label": "Wikipedia"},
        {"url": "https://www.reddit.com", "label": "Reddit"},
        {"url": "https://www.youtube.com", "label": "YouTube"},
        {"url": "https://www.twitter.com", "label": "Twitter"},
        {"url": "https://www.linkedin.com", "label": "LinkedIn"},
        {"url": "https://www.bbc.com", "label": "BBC"}
    ]

    # Collect user inputs, use defaults if empty
    links = [
        {"url": button1_url or default_links[0]["url"], "label": button1_label or default_links[0]["label"]},
        {"url": button2_url or default_links[1]["url"], "label": button2_label or default_links[1]["label"]},
        {"url": button3_url or default_links[2]["url"], "label": button3_label or default_links[2]["label"]},
        {"url": button4_url or default_links[3]["url"], "label": button4_label or default_links[3]["label"]},
        {"url": button5_url or default_links[4]["url"], "label": button5_label or default_links[4]["label"]},
        {"url": button6_url or default_links[5]["url"], "label": button6_label or default_links[5]["label"]},
        {"url": button7_url or default_links[6]["url"], "label": button7_label or default_links[6]["label"]},
        {"url": button8_url or default_links[7]["url"], "label": button8_label or default_links[7]["label"]},
        {"url": button9_url or default_links[8]["url"], "label": button9_label or default_links[8]["label"]},
        {"url": button10_url or default_links[9]["url"], "label": button10_label or default_links[9]["label"]}
    ]

    # Handle filename
    if not filename:
        filename = "buttons.html"
    if not filename.lower().endswith('.html'):
        filename += '.html'

    # HTML template matching the provided buttons.html
    html_content = f"""
<html>
<head>
    <title>Programmable Link Buttons</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
            background-color: #f0f0f0;
        }}
        h1 {{
            color: #333;
        }}
        .pill-button-0 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-0:hover {{
            background-color: #0056b3;
            transform: scale(1.05);
        }}
        .pill-button-0:active {{
            transform: scale(0.95);
        }}
        .pill-button-1 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #28a745;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-1:hover {{
            background-color: #218838;
            transform: scale(1.05);
        }}
        .pill-button-1:active {{
            transform: scale(0.95);
        }}
        .pill-button-2 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #6f42c1;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-2:hover {{
            background-color: #5a32a3;
            transform: scale(1.05);
        }}
        .pill-button-2:active {{
            transform: scale(0.95);
        }}
        .pill-button-3 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #fd7e14;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-3:hover {{
            background-color: #d8650e;
            transform: scale(1.05);
        }}
        .pill-button-3:active {{
            transform: scale(0.95);
        }}
        .pill-button-4 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #17a2b8;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-4:hover {{
            background-color: #117a8b;
            transform: scale(1.05);
        }}
        .pill-button-4:active {{
            transform: scale(0.95);
        }}
        .pill-button-5 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #dc3545;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-5:hover {{
            background-color: #b02a37;
            transform: scale(1.05);
        }}
        .pill-button-5:active {{
            transform: scale(0.95);
        }}
        .pill-button-6 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #c82333;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-6:hover {{
            background-color: #a71d2a;
            transform: scale(1.05);
        }}
        .pill-button-6:active {{
            transform: scale(0.95);
        }}
        .pill-button-7 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #1da1f2;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-7:hover {{
            background-color: #1a91da;
            transform: scale(1.05);
        }}
        .pill-button-7:active {{
            transform: scale(0.95);
        }}
        .pill-button-8 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #0077b5;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-8:hover {{
            background-color: #005983;
            transform: scale(1.05);
        }}
        .pill-button-8:active {{
            transform: scale(0.95);
        }}
        .pill-button-9 {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #6c757d;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.1s;
        }}
        .pill-button-9:hover {{
            background-color: #5a6268;
            transform: scale(1.05);
        }}
        .pill-button-9:active {{
            transform: scale(0.95);
        }}
    </style>
</head>
<body>
    <h1>Link Launcher</h1>
    <div id="buttonContainer"></div>

    <script>
        // Array of URLs and corresponding button labels
        const links = [
            {', '.join(f'{{ url: "{escape_js_string(link["url"])}", label: "{escape_js_string(link["label"])}" }}' for link in links)}
        ];

        // Dynamically create pill-shaped buttons with specific labels and styles
        const container = document.getElementById('buttonContainer');
        links.forEach((link, index) => {{
            const button = document.createElement('button');
            button.className = `pill-button-${{index}}`;
            button.textContent = link.label;
            button.onclick = () => window.open(link.url, '_blank');
            container.appendChild(button);
            container.appendChild(document.createElement('br'));
        }});
    </script>
</body>
</html>
    """

    # Write HTML content to a temporary file
    try:
        # Create a temporary file with the user-specified filename
        temp_file = os.path.join(tempfile.gettempdir(), filename)
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return temp_file
    except Exception as e:
        raise Exception(f"Failed to write temporary file: {e}")

# Create Gradio interface
with gr.Blocks(css="""
    body { font-family: Arial, sans-serif; background-color: #f0f0f0; text-align: center; }
    h1 { color: #333; }
    .gr-button { 
        display: inline-block; 
        margin: 10px; 
        padding: 12px 24px; 
        font-size: 16px; 
        font-weight: bold; 
        color: #fff; 
        background-color: #007bff; 
        border: none; 
        border-radius: 25px; 
        cursor: pointer; 
        transition: background-color 0.3s, transform 0.1s; 
    }
    .gr-button:hover { 
        background-color: #0056b3; 
        transform: scale(1.05); 
    }
    .gr-button:active { 
        transform: scale(0.95); 
    }
""") as demo:
    gr.Markdown("# Custom Link Programmer")
    
    # Create input fields for 10 buttons
    inputs = []
    for i in range(10):
        with gr.Row():
            label = gr.Textbox(label=f"Button {i+1} Name", value=["LH7860", "Google", "GitHub", "Stack Overflow", "Wikipedia", "Reddit", "YouTube", "Twitter", "LinkedIn", "BBC"][i], placeholder=f"e.g., Button {i+1}")
            url = gr.Textbox(label=f"Button {i+1} URL", value=["localhost:7860", "https://www.google.com", "https://www.github.com", "https://www.stackoverflow.com", "https://www.wikipedia.org", "https://www.reddit.com", "https://www.youtube.com", "https://www.twitter.com", "https://www.linkedin.com", "https://www.bbc.com"][i], placeholder="e.g., https://example.com")
            inputs.extend([label, url])
    
    # Filename input
    filename = gr.Textbox(label="Output Filename", value="buttons.html", placeholder="e.g., buttons.html")
    
    # Submit button
    submit = gr.Button("Save Custom Link Maker")
    
    # Output for file download
    output = gr.File(label="Download your custom HTML file")
    
    # Connect button to generate_html function
    submit.click(
        fn=generate_html,
        inputs=inputs + [filename],
        outputs=output
    )

# Launch the interface
demo.launch()