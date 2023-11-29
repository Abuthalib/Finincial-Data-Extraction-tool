import json

data = {
    "name": "John Doe",
    "personal_details": {
        "email": "johndoe@example.com",
        "phone": "123-456-7890",
    },
    "qualifications": [
        "Bachelor of Science in Computer Science",
        "Master of Business Administration",
    ],
    "skills": [
        "Programming: Python, Java, C++",
        "Databases: MySQL, PostgreSQL",
        "Machine Learning: TensorFlow, PyTorch",
    ],
    "experience": [
        {
            "company": "Google",
            "title": "Software Engineer",
            "dates": "2015-2020",
        },
        {
            "company": "Amazon",
            "title": "Data Scientist",
            "dates": "2020-present",
        },
    ],
}

import streamlit as st
import json

with open('data.json') as infile:
    data = json.load(infile)

# Define CSS styles for boxes
box_style = """
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
"""

# Display resume data within boxes
with st.container(style=box_style):
    st.title("Resume Data")
    st.write("**Name:** {}".format(data["name"]))

with st.container(style=box_style):
    st.write("**Personal Details:**")
    st.write("- Email: {}".format(data["personal_details"]["email"]))
    st.write("- Phone: {}".format(data["personal_details"]["phone"]))

with st.container(style=box_style):
    st.write("**Qualifications:**")
    for qualification in data["qualifications"]:
        st.write("- {}".format(qualification))

with st.container(style=box_style):
    st.write("**Skills:**")
    for skill in data["skills"]:
        st.write("- {}".format(skill))

with st.container(style=box_style):
    st.write("**Experience:**")
    for experience in data["experience"]:
        st.write("- **Company:** {}".format(experience["company"]))
        st.write("- **Title:** {}".format(experience["title"]))
        st.write("- **Dates:** {}".format(experience["dates"]))
