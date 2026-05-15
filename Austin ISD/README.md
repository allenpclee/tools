# Austin Area ISD Interactive Map

An interactive, web-based map that visualizes the top Independent School Districts (ISDs), city boundaries, and top-rated public schools within the Austin, Texas area.

## Features

- **ISD Highlighting**: Displays interactive boundaries for Eanes, Dripping Springs, Leander, Lake Travis, Liberty Hill, and Round Rock ISDs. Clicking on any district will bold its boundary and highlight the area.
- **City Limits**: Outlines the official city limits in the Austin area with clear central labels.
- **Top Public Schools**: Plots precise pins for 18 of the top-rated K-12 public schools across these districts. Hovering over a pin reveals the school's name, and clicking the pin provides more details.
- **Clean UI**: Uses CartoDB Positron base maps to provide a distraction-free, visual-first viewing experience.

## How to Run

Because this map loads geographic shape data from local `.geojson` files, modern web browsers will block the map from loading if you simply double-click the `index.html` file (due to standard CORS security policies).

To view the map properly, you need to run a lightweight local web server. You can easily do this using Python, which is already installed on most systems.

### Steps:

1. **Open a Terminal or Command Prompt** and navigate to this folder (`Austin ISD`).
2. **Start the local server** by running the following command:
   ```bash
   python -m http.server 8000
   ```
3. **Open your Web Browser** and go to:
   [http://localhost:8000](http://localhost:8000)

The map will load instantly with all boundaries, styles, and school pins completely intact.

## File Structure

- `index.html`: The main web application containing the Leaflet.js map logic and styling.
- `cities.geojson`: US Census boundary data for the city limits in the Austin region.
- `isds.geojson`: US Census boundary data specifically filtered for the 6 highlighted school districts.
- `schools.geojson`: Exact geocoded coordinates for the top public schools across the selected districts.
