import streamlit as st

st.set_page_config(page_title="Dynamic Event Planner", page_icon="🎉")
st.title("AI-Style Event Planner")
st.write("Enter any event name and the app will generate tasks dynamically!")

# Input Section
event_name = st.text_input("Event Name ")
event_date = st.date_input("Event Date")
event_duration = st.number_input("Event Duration (hours)", min_value=1, max_value=24, value=4)
num_attendees = st.number_input("Number of Attendees", min_value=1, value=50)

# Budget estimation per attendee (simplified)
budget_per_person = 500

# Session state
if "tasks_done" not in st.session_state:
    st.session_state.tasks_done = []

# Simple dynamic task generator
def generate_tasks(event_name):
    name_lower = event_name.lower()
    tasks = []

    # Detect event type by keywords
    if any(word in name_lower for word in ["birthday", "anniversary", "party"]):
        tasks = [
            f"Book party venue for '{event_name}'",
            f"Send invitations for '{event_name}'",
            f"Order cake for '{event_name}'",
            f"Decorate venue for '{event_name}'",
            f"Plan entertainment for '{event_name}'"
        ]
    elif any(word in name_lower for word in ["conference", "summit", "meetup"]):
        tasks = [
            f"Book conference venue for '{event_name}'",
            f"Arrange speakers for '{event_name}'",
            f"Prepare agenda for '{event_name}'",
            f"Set up registration for '{event_name}'",
            f"Arrange catering for '{event_name}'"
        ]
    elif any(word in name_lower for word in ["workshop", "training", "seminar"]):
        tasks = [
            f"Book workshop venue for '{event_name}'",
            f"Prepare materials for '{event_name}'",
            f"Send invites for '{event_name}'",
            f"Arrange refreshments for '{event_name}'",
            f"Set up equipment for '{event_name}'"
        ]
    elif any(word in name_lower for word in ["concert", "music", "performance"]):
        tasks = [
            f"Book stage and venue for '{event_name}'",
            f"Arrange performers for '{event_name}'",
            f"Set up sound and lighting for '{event_name}'",
            f"Sell tickets for '{event_name}'",
            f"Arrange security and logistics for '{event_name}'"
        ]
    else:
        # Generic fallback for unknown events
        tasks = [
            f"Book venue for '{event_name}'",
            f"Plan activities for '{event_name}'",
            f"Send invitations for '{event_name}'",
            f"Arrange refreshments for '{event_name}'",
            f"Decorate venue for '{event_name}'"
        ]
    return tasks

# Generate event plan
if st.button("Generate Event Plan") and event_name.strip():
    tasks = generate_tasks(event_name)
    st.session_state.generated = True
    st.session_state.all_tasks = tasks
    st.session_state.tasks_done = [False] * len(tasks)

# Display Event Plan
if st.session_state.get("generated", False):
    st.success(f"✅ Event Plan for **{event_name}** on {event_date}")

    # Dynamic schedule
    st.subheader("🕒 Suggested Schedule")
    num_tasks = len(st.session_state.all_tasks)
    hours_per_task = event_duration / num_tasks
    for i, task in enumerate(st.session_state.all_tasks):
        st.write(f"Task {i+1}: {task} ({hours_per_task:.1f} hours)")

    # Task checklist
    st.subheader("📋 Task Checklist")
    for i, task in enumerate(st.session_state.all_tasks):
        st.session_state.tasks_done[i] = st.checkbox(task, value=st.session_state.tasks_done[i])

    # Budget estimation
    budget = num_attendees * budget_per_person
    st.subheader("💰 Estimated Budget (INR)")
    st.write(f"Estimated budget for {num_attendees} attendees: **₹{budget:,}**")
