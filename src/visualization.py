"""
visualization.py
Animated pie chart for risk contributions with interactive sliders.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider


def animate_pie_chart(asset_names, get_risk_contributions, initial_weights):
    """
    Animate a pie chart of risk contributions with interactive sliders for weights.
    Args:
        asset_names (list): List of asset names.
        get_risk_contributions (callable): Function returning risk contributions given weights.
        initial_weights (np.ndarray): Initial portfolio weights.
    """
    num_assets = len(asset_names)
    weights = initial_weights.copy()

    # Dark theme setup
    plt.style.use('dark_background')
    fig, ax = plt.subplots(facecolor='#181818')
    fig.patch.set_facecolor('#181818')
    plt.subplots_adjust(left=0.1, bottom=0.25)

    # 3D effect: explode and shadow
    colors = ['#00bfff', '#ff69b4', '#32cd32', '#ffa500', '#ff6347', '#9370db']
    explode = [0.08] * len(asset_names)  # pop out all slices a bit
    pie, texts, autotexts = ax.pie(
        get_risk_contributions(weights),
        labels=asset_names,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors[:len(asset_names)],
        explode=explode,
        shadow=True,
        wedgeprops={"edgecolor": "#222", "linewidth": 1.5}
    )
    ax.set_title('Portfolio Risk Contribution', color='white', fontsize=16)
    for text in texts + autotexts:
        text.set_color('white')

    # Sliders for each asset weight
    sliders = []
    slider_axes = []
    for i in range(num_assets):
        ax_slider = plt.axes([0.1, 0.1 - i*0.04, 0.8, 0.03], facecolor='#222')
        slider = Slider(
            ax_slider, asset_names[i], 0, 1, valinit=weights[i], valstep=0.01,
            color=colors[i % len(colors)]
        )
        sliders.append(slider)
        slider_axes.append(ax_slider)

    def update(val):
        # Read weights from sliders and normalize
        w = np.array([slider.val for slider in sliders])
        w = np.clip(w, 0, 1)
        if w.sum() == 0:
            w = np.ones_like(w) / len(w)
        else:
            w = w / w.sum()
        rc = get_risk_contributions(w)
        ax.clear()
        pie, texts, autotexts = ax.pie(
            rc,
            labels=asset_names,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors[:len(asset_names)],
            explode=explode,
            shadow=True,
            wedgeprops={"edgecolor": "#222", "linewidth": 1.5}
        )
        ax.set_title('Portfolio Risk Contribution', color='white', fontsize=16)
        for text in texts + autotexts:
            text.set_color('white')
        fig.canvas.draw_idle()

    for slider in sliders:
        slider.on_changed(update)

    plt.show()
