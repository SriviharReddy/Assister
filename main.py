"""
Assister - AI Voice Assistant App
Main entry point for the Flet application
"""

import flet as ft


class AssisterApp:
    """Main application class for Assister voice assistant."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.is_listening = False
        self.setup_page()
        self.build_ui()

    def setup_page(self):
        """Configure page settings and theme."""
        self.page.title = "Assister"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 0
        self.page.bgcolor = "#0a0a0f"
        
        # Custom dark theme with accent colors
        self.page.theme = ft.Theme(
            color_scheme_seed="#6366f1",
        )
        
        self.page.window.width = 400
        self.page.window.height = 750

    def toggle_listening(self, e):
        """Toggle the listening state of the microphone."""
        self.is_listening = not self.is_listening
        
        if self.is_listening:
            self.mic_button.icon = ft.Icons.MIC
            self.mic_button.bgcolor = "#6366f1"
            self.mic_container.border = ft.Border.all(3, "#6366f1")
            self.status_text.value = "Listening..."
            self.status_text.color = "#6366f1"
            # Show pulsing animation
            self.pulse_ring.opacity = 1
        else:
            self.mic_button.icon = ft.Icons.MIC_NONE
            self.mic_button.bgcolor = "#2a2a3e"
            self.mic_container.border = ft.Border.all(2, "#3a3a4e")
            self.status_text.value = "Tap to speak"
            self.status_text.color = "#64748b"
            self.pulse_ring.opacity = 0
        
        self.page.update()

    def nav_click(self, e):
        """Handle navigation bar clicks."""
        index = e.control.selected_index
        destinations = ["home", "history", "notes", "calendar", "settings"]
        print(f"Navigating to: {destinations[index]}")
        # TODO: Implement navigation logic
        
    def build_ui(self):
        """Build the main user interface."""
        
        # Pulsing ring animation (behind mic button)
        self.pulse_ring = ft.Container(
            width=200,
            height=200,
            border_radius=100,
            bgcolor=None,
            border=ft.Border.all(2, "#6366f1"),
            opacity=0,
            animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
        )
        
        # Main mic button
        self.mic_button = ft.IconButton(
            icon=ft.Icons.MIC_NONE,
            icon_size=80,
            icon_color="#ffffff",
            bgcolor="#2a2a3e",
            on_click=self.toggle_listening,
            style=ft.ButtonStyle(
                shape=ft.CircleBorder(),
                animation_duration=200,
            ),
        )
        
        # Mic container with border
        self.mic_container = ft.Container(
            content=self.mic_button,
            width=160,
            height=160,
            border_radius=80,
            border=ft.Border.all(2, "#3a3a4e"),
            alignment=ft.Alignment(0, 0),  # center
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=30,
                color="#6366f120",
                offset=ft.Offset(0, 10),
            ),
        )
        
        # Status text
        self.status_text = ft.Text(
            "Tap to speak",
            size=18,
            color="#64748b",
            weight=ft.FontWeight.W_500,
            animate_opacity=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
        )
        
        # App title/greeting
        greeting = ft.Column(
            controls=[
                ft.Text(
                    "Assister",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color="#ffffff",
                ),
                ft.Text(
                    "Your AI assistant",
                    size=16,
                    color="#64748b",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
        )
        
        # Center content with mic button
        center_content = ft.Column(
            controls=[
                greeting,
                ft.Container(height=60),  # Spacer
                ft.Stack(
                    controls=[
                        ft.Container(
                            content=self.pulse_ring,
                            alignment=ft.Alignment(0, 0),
                        ),
                        ft.Container(
                            content=self.mic_container,
                            alignment=ft.Alignment(0, 0),
                        ),
                    ],
                    width=200,
                    height=200,
                ),
                ft.Container(height=30),  # Spacer
                self.status_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        )
        
        # Bottom navigation bar
        nav_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="Home",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.HISTORY_OUTLINED,
                    selected_icon=ft.Icons.HISTORY,
                    label="History",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.NOTE_OUTLINED,
                    selected_icon=ft.Icons.NOTE,
                    label="Notes",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.CALENDAR_MONTH_OUTLINED,
                    selected_icon=ft.Icons.CALENDAR_MONTH,
                    label="Calendar",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icons.SETTINGS,
                    label="Settings",
                ),
            ],
            bgcolor="#12121a",
            indicator_color="#6366f130",
            label_behavior=ft.NavigationBarLabelBehavior.ALWAYS_SHOW,
            on_change=self.nav_click,
            selected_index=0,
            height=70,
        )
        
        # Main layout
        self.page.add(
            ft.Container(
                content=ft.Column(
                    controls=[
                        center_content,
                        nav_bar,
                    ],
                    spacing=0,
                    expand=True,
                ),
                expand=True,
                bgcolor="#0a0a0f",
            )
        )


def main(page: ft.Page):
    """Main entry point."""
    AssisterApp(page)


if __name__ == "__main__":
    ft.run(main)
