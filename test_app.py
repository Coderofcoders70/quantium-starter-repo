from dash.testing.composite import DashComposite
from app import app 

# To check the header is present in app.py
def test_001_header_exists(dash_duo):

    dash_duo.start_server(app)
    
    header = dash_duo.find_element("h1")
    
    assert header.text == "Pink Morsel Sales Visualizer"

# To check the visualization is present in app.py
def test_002_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    
    graph = dash_duo.find_element("#sales-line-chart")
    
    assert graph is not None

# To check the region picker is present in app.py
def test_003_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    
    region_picker = dash_duo.find_element("#region-filter")
    
    assert region_picker is not None