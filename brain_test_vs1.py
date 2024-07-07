import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets['OPENAI_SECRET_KEY'])

# Set title
#st.title('Brain-based Career and Course Advisor AI App')

# Display image
st.image("Apps Logo.png")

# Display welcome
#st.write('Welcome to Brain-based Career and Course Advisor AI App!')

# Define the prompt
prompt = """
I am a career advisor for SPM/STPM students. I help them choose suitable educational and career paths based on their brain hemisphere dominance. I provide advice on career options and courses. I also suggest institutions in Malaysia offering these courses. My tone is friendly. Provide tailored advice based on brain dominance results.
"""

# Make the API call
response = client.chat.completions.create(
    #engine="davinci-codex",
    model="gpt-4o",  # Use the Codex engine for coding tasks
    messages=[{
              "role":"system",
              "content":prompt
         },
          ],
          max_tokens=300
      )

# Print the response
#print(response.choices[0].text.strip())

# Create a new model
#def brainid (msg,sysprompt):
 # Brain_response = client.chat.completions.create(
 #     model="gpt-4o",
 #     messages=[{
 #         "role":"system",
 #         "content":sysprompt
#      },
 #     {
 #         "role":"user",
 #         "content":msg
 #     }
 #     ],
 #     max_tokens=300
 # )

#  Brain = Brain_response.choices[0].message.content
 # return Brain

import streamlit as st

class BrainBasedCareerAdvisor:
    def __init__(self):
        self.questions = [
            "1) Do you prefer a) working with numbers or b) creating art?",
            "2) What are your favorite activities, a) like drawing or b) solving puzzles?",
            "3) Do you enjoy a) reading or b) watching movie?",
            "4) Do you like to a) follow instructions or b) create your own way of doing things?",
            "5)Do you enjoy a) logic games or b) creative storytelling?",
            "6) Do you prefer a) detailed tasks or b) big-picture ideas?",
            "7) Do you like to work in a) an organized environment or b) a more flexible one?",
            "8) Do you follow a) a schedule or b) do things spontaneously?",
            "9) Do you prefer a) structured learning or b) hands-on projects?",
            "10) Do you enjoy a)critical thinking or b) imaginative thinking more?"
        ]
        self.career_suggestions = {
            'left_brained': ['Engineer', 'Accountant', 'Data Analyst','Financial Analyst','Software Developer','Doctor','Lawyer','Architect','Economist','Programmer'],
            'right_brained': ['Multimedia Animator', 'Writer', 'Fashion Designer','Interior Designer', 'Musician','Photographer','Journalist','Dancer','Actor','Writer'],
            'balanced': ['Educator/Teacher', 'Entrepreneur', 'IT Manager', 'UI/UX Designer,''Marketing Manager','Business Analyst','Researcher','Data Scientist','Project Manager','Lecturer']
        }
        self.course_suggestions = {
            'Engineer': ['Mechanical Engineering', 'Electrical Engineering', 'Civil Engineering'],
            'Accountant': ['Accounting', 'Finance', 'Business Administration'],
            'Data Analyst': ['Computer Science', 'Information Technology', 'Data Science'],
            'Financial Analyst': ['Accounting', 'Financial Management', 'Financial Analysis'],
            'Software Developer': ['Computer Science', 'Information Technology', 'Software Engineering'],
            'Doctor': ['Medical Science', 'Surgery', 'Dentistry'],
            'Lawyer': ['Law', 'Criminal Law', 'Shariah Law'],
            'Architect' : ['Architecture', 'Interior Design', 'Urban Planning'],
            'Economist': ['Economics', 'Financial Economics', 'Macroeconomics'],
            'Programmer': ['Software Engineering', 'Computer Science', 'Information Technology'],
            'Multimedia Animator': ['Animation', 'Multimedia', 'Graphic Design'],
            'Writer': ['Creative Writing', 'Storytelling', 'Poetry'],
            'Fashion Designer': ['Fashion Design', 'Textile Design', 'Clothes Design'],
            'Interior Designer': ['Interior Design', 'Architecture', 'Interior Planning'],
            'Musician': ['Music Composition', 'Music Performance', 'Music Theory'],
            'Photographer': ['Photography', 'Filmmaking', 'Videography'],
            'Journalist': ['Journalism', 'Public Relations', 'Media Communication'],
            'Dancer': ['Dance', 'Music Performance', 'Theater'],
            'Actor': ['Acting', 'Filmmaking', 'Theater'],
            'Writer': ['Creative Writing', 'Literature', 'Script Writing'],
            'Educator/Teacher': ['Education', 'TESL', 'Early Chilhood Education'],
            'Entrepreneur': ['Business Management', 'Marketing', 'Economics'],
            'IT Manager': ['Information Technology', 'Computer Science', 'Software Engineer'],
            'UI/UX Designer': ['User Interface Design', 'User Experience Design', 'Graphic Design'],
            'Marketing Manager': ['Marketing', 'Sales', 'Customer Service'],
            'Business Analyst': ['Business Analysis', 'Finance', 'Economics'],
            'Researcher': ['Research', 'Data Analysis', 'Data Visualization'],
            'Data Scientist': ['Data Science', 'Machine Learning', 'Big Data'],
            'Project Manager': ['Project Management', 'Project Planning', 'Project Execution'],

            'Entrepreneur': ['Business Management', 'Marketing', 'Economics'],
            'Manager': ['Business Administration', 'Human Resources', 'Project Management'],
            'Lecturer': ['Information Technology', 'English', 'Science'],
        }
        self.universities = {
            'Computer Science': ['UNISEL', 'UTM', 'UM', 'UiTM'], 
            'Information Technology': ['UNISEL', 'UTM', 'UM', 'UiTM'],
            'Data Science': ['UNISEL', 'UTM', 'UM', 'Taylor\'s University'],
            'Animation' : ['UNISEL', 'Multimedia University'],
            'Multimedia' : ['UNISEL', 'UTM', 'UM', 'UiTM'],
            'Communication': ['UNISEL', 'UiTM','UTM','APU'],
            'Graphic Design': ['UNISEL', 'UiTM'],
            'Research': ['UNISEL', 'UTM', 'UM', 'UiTM'],
            'Business Administration': ['UNISEL', 'UTM', 'UM', 'UiTM'],
            'Finance': ['UNISEL', 'UTM', 'UM', 'UiTM'],
            'Art': ['UiTM', 'Aswara'],
            'Mechanical Engineering': ['UNISEL', 'University of Malaya', 'UTM'],
            'Accounting': ['UNISEL', 'Taylor\'s University', 'HELP University'],
            'Biology': ['UNISEL', 'UKM', 'USM'],
            'Fine Arts': ['UNISEL', 'UITM', 'Limkokwing University'],
            'Education': ['UNISEL', 'UPSI', 'UTM'],
            'TESL': ['UNISEL', 'UiTM', 'UPSI'],
            'Early Chilhood Education': ['UNISEL', 'UPSI'],
            'Electrical Engineering': ['UTEM', 'University of Malaya', 'UTM'],
            'Mechanical Engineering': ['UTEM', 'University of Malaya', 'UTM'],
            'Civil Engineering': ['UTEM', 'University of Malaya', 'UTM'],
            'Business Management': ['UNISEL', 'Taylor\'s University', 'Sunway University']
        }

    def determine_brain_dominance(self, answers):
        left_brain_count = sum(1 for answer in answers if answer == 'A')
        right_brain_count = sum(1 for answer in answers if answer == 'B')

        if left_brain_count > right_brain_count:
            return 'left_brained'
        elif right_brain_count > left_brain_count:
            return 'right_brained'
        else:
            return 'balanced'

    def suggest_careers_and_courses(self, dominance):
        careers = self.career_suggestions[dominance]
        return careers

    def get_course_and_universities(self, chosen_career):
        courses = self.course_suggestions.get(chosen_career, [])
        universities = {course: self.universities.get(course, []) for course in courses}
        return courses, universities

advisor = BrainBasedCareerAdvisor()

def main():
    #st.title("Brain-Based Career Advisor")

    st.write("Welcome to Brain-based Career and Course Advisor. I will ask you 10 questions to determine your brain dominance and suggest suitable careers and courses for you.")

    answers = []
    for i, question in enumerate(advisor.questions):
        st.markdown(f"<h6>{question}</h6>", unsafe_allow_html=True)
        answer = st.radio("", ('A', 'B'), key=i)
        answers.append(answer)
        st.markdown(f"<br>", unsafe_allow_html=True)

    if st.button("Submit"):
        dominance = advisor.determine_brain_dominance(answers)
        st.write(f"Based on your answers, you are {dominance.replace('_', ' ')}.")

        careers = advisor.suggest_careers_and_courses(dominance)
        st.write("Here are some career options for you:")

        st.markdown("Which career are you most interested in?", unsafe_allow_html=True)

        chosen_career = st.selectbox('', careers)

        if chosen_career:
            courses, universities = advisor.get_course_and_universities(chosen_career)
            st.write(f"To pursue a career as a {chosen_career}, you can consider the following courses:")
            for idx, course in enumerate(courses, 1):
                st.write(f"{idx}. <b>{course}</b>", unsafe_allow_html=True)
                if course in universities:
                   st.write("  Universities offering this course:")
                for uni in universities[course]:
                  st.write(f"  - {uni} ")

if __name__ == '__main__':
    main()
