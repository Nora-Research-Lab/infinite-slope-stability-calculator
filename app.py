import gradio as gr
from infinite_slope_stability_calculator import calculate_factor_of_safety

def calculate_wrapper(c_prime, phi_prime, beta, gamma, z, h_w):
    # Validate h_w <= z
    if h_w > z:
        return None, "", "Warning: Water height h_w cannot exceed depth z"
    
    fs, classification = calculate_factor_of_safety(c_prime, phi_prime, beta, gamma, z, h_w)
    
    # Determine if we need to show a warning based on FS value
    warning = "Warning: Slope is unstable!" if fs < 1.0 else ""
    
    return round(fs, 3), classification, warning

with gr.Blocks() as demo:
    gr.Markdown("## Infinite Slope Stability Calculator")
    gr.Markdown("Calculate the factor of safety against shallow translational sliding.")
    
    with gr.Row():
        with gr.Column():
            c_prime = gr.Number(label="Effective Cohesion c' (kPa)", value=20.0)
            phi_prime = gr.Number(label="Effective Friction Angle φ' (degrees)", value=30.0)
            beta = gr.Number(label="Slope Angle β (degrees)", value=25.0)
        with gr.Column():
            gamma = gr.Number(label="Soil Unit Weight γ (kN/m³)", value=18.0)
            z = gr.Number(label="Depth to Failure Plane z (m)", value=5.0)
            h_w = gr.Number(label="Water Height Above Failure Plane h_w (m)", value=1.0)
    
    calculate_btn = gr.Button("Calculate Factor of Safety")
    
    with gr.Row():
        fs_output = gr.Number(label="Factor of Safety (FS)")
        classification_output = gr.Label(label="Stability Classification")
    
    warning_output = gr.Textbox(label="Warnings", interactive=False)
    
    calculate_btn.click(
        fn=calculate_wrapper,
        inputs=[c_prime, phi_prime, beta, gamma, z, h_w],
        outputs=[fs_output, classification_output, warning_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
