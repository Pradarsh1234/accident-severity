import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('decision_tree_model.pkl')

# Mapping dictionaries
accident_spot_mapping = {'Bottleneck': 0, 'Road hump or Rumble strips': 1, 'Cross roads': 2, 'Bridge': 3, 'Junction': 4, 'Curves': 5, 'Culvert': 6, 'Narrow road': 7, 'T Junction': 8, 'Railway crossing': 9, 'Offset': 10, 'Circle': 11, 'Y Junction': 12, 'Staggered junction': 13, 'More than four arms': 14, 'Rail Crossing manned': 15, 'Round about or Circle': 16, 'Rail Crossing Unmanned': 17}
accident_location_mapping = {'Rural Areas': 0, 'City/Town': 1, 'Villages settlement': 2}
collision_type_mapping = {'Drowned': 0, 'Skidding or Self accident': 1, 'Hit bicyclist': 2, 'Head on': 3, 'Rear end': 4, 'Hit puchcart': 5, 'Hit fixed object': 6, 'Overturning': 7, 'Vehicle to Vehicle': 8, 'Hit pedestrian': 9, 'Hit animal': 10, 'Side impact or Right angle': 11, 'Side swipe': 12, 'Run Off Road': 13, 'Hit and Run': 14, 'Right Turn Collision': 15, 'Hit parked vehicle': 16, 'Hit pedal cyclist': 17}
road_character_mapping = {'Curve': 0, 'Hump': 1, 'Dip or trough': 2, 'Straight and flat': 3, 'Curve and Incline': 4, 'Incline': 5, 'Crest of hill': 6, 'Slight Curve': 7, 'Sharp Curve': 8, 'Steep Incline or Climb': 9, 'Gentle Incline or Climb': 10}
road_type_mapping = {'State Highway': 0, 'Village Road': 1, 'NH': 2, 'One way': 3, 'City or Town Road': 4, 'Major District Road': 5, 'Two way': 6, 'Sub Arterial': 7, 'Service Road': 8, 'Feeder Road': 9, 'Expressway': 10, 'Arterial': 11, 'Mixed': 12, 'Minor District Road': 13, 'Residential Street': 14, 'Forest Road': 15}
severity_mapping = {0: 'Grievous Injury', 1: 'Fatal', 2: 'Damage Only', 3: 'Simple Injury'}

st.title('Accident Severity Prediction')

# Get data from user input
accident_spot = st.selectbox('Accident Spot', list(accident_spot_mapping.keys()))
accident_location = st.selectbox('Accident Location', list(accident_location_mapping.keys()))
collision_type = st.selectbox('Collision Type', list(collision_type_mapping.keys()))
road_character = st.selectbox('Road Character', list(road_character_mapping.keys()))
road_type = st.selectbox('Road Type', list(road_type_mapping.keys()))

if st.button('Predict'):
    # Convert form data to numerical values using mapping
    data = {
        'Accident_Spot': accident_spot_mapping[accident_spot],
        'Accident_Location': accident_location_mapping[accident_location],
        'Collision_Type': collision_type_mapping[collision_type],
        'Road_Character': road_character_mapping[road_character],
        'Road_Type': road_type_mapping[road_type]
    }

    # Convert to DataFrame
    data_df = pd.DataFrame([data])

    # Predict severity
    severity_prediction = model.predict(data_df)[0]

    # Convert numerical severity to categorical value
    severity_categorical = severity_mapping[severity_prediction]

    st.write(f'Predicted Severity: {severity_categorical}')