---
name: Artisanal Hearth
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d4c4b7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9c8e82'
  outline-variant: '#50453b'
  surface-tint: '#f0bd8b'
  primary: '#f2be8c'
  on-primary: '#482904'
  primary-container: '#d4a373'
  on-primary-container: '#5b3912'
  inverse-primary: '#7d562d'
  secondary: '#ffb95a'
  on-secondary: '#462a00'
  secondary-container: '#c68315'
  on-secondary-container: '#3d2400'
  tertiary: '#dfc2b1'
  on-tertiary: '#3f2c20'
  tertiary-container: '#c3a796'
  on-tertiary-container: '#503c2f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcbd'
  primary-fixed-dim: '#f0bd8b'
  on-primary-fixed: '#2c1600'
  on-primary-fixed-variant: '#623f18'
  secondary-fixed: '#ffddb6'
  secondary-fixed-dim: '#ffb95a'
  on-secondary-fixed: '#2a1800'
  on-secondary-fixed-variant: '#643f00'
  tertiary-fixed: '#fbddca'
  tertiary-fixed-dim: '#dec1af'
  on-tertiary-fixed: '#28180d'
  on-tertiary-fixed-variant: '#574335'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  section-padding: 80px
---

## Brand & Style

This design system is built to evoke the sensory experience of a high-end artisanal bakery at dawn—the quiet, warm glow of ovens against a cool, dark kitchen. The brand personality is grounded, sophisticated, and deeply welcoming, targeting an audience that appreciates the slow craft of fermentation and the heritage of baking.

The design style is **Minimalist with Tactile accents**. It leverages heavy whitespace (rendered here as "dark space") and premium typography to create an editorial feel. While the UI remains functional and clean, the use of subtle shadows and rich, earthen gradients provides a sense of physical depth, making the digital experience feel as tangible as a loaf of sourdough.

## Colors

The palette is anchored in a deep, atmospheric foundation to highlight the "warmth" of the content. 

- **Primary (Golden Amber):** Used for key brand moments and active states, mimicking the perfect crust of a loaf.
- **Secondary (Oven Glow):** A brighter amber for high-priority calls to action and highlights.
- **Tertiary (Chocolate Brown):** A rich, warm mid-tone used for containers and subtle layering.
- **Neutral (Deep Charcoal):** The primary background color, providing a modern, matte finish that allows golden accents to pop.

Backgrounds should utilize subtle radial gradients transitioning from the neutral charcoal at the edges to a slightly warmer tertiary brown in the center of main content areas to simulate a hearth's glow.

## Typography

This design system employs a classic typographic contrast. **Noto Serif** is used for all headings to establish a sense of tradition, heritage, and "slow" craft. It should be typeset with slightly tighter letter spacing for a premium, editorial look.

**Be Vietnam Pro** serves as the functional workhorse. Its contemporary, friendly curves balance the formality of the serif, ensuring the interface feels modern and approachable. Labels and small navigation items should use the sans-serif in uppercase with generous letter spacing to maintain legibility against dark backgrounds.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop to ensure the content feels curated and contained, centered within the viewport. A 12-column grid is used for desktop, while a 4-column grid is used for mobile devices.

Spacing is generous, prioritizing "breathability." Large vertical gaps (Section Padding) are used to separate different stories—such as the bakery's history, the ingredient sourcing, and the daily menu—ensuring the user is never overwhelmed. Use the 8px base unit to define all internal padding and margins to maintain a rhythmic, mathematical consistency.

## Elevation & Depth

In this design system, depth is created through **Tonal Layers** and **Ambient Shadows**. Because the background is dark, traditional black shadows are replaced with deep brown or "burnt" amber shadows (e.g., `#000000` at 40% opacity with a slight warm tint).

1.  **Base Layer:** The Charcoal background (`#1A1A1A`).
2.  **Surface Layer:** Dark Chocolate (`#2A1F18`) containers used for cards and menus.
3.  **Floating Layer:** Elements like navigation bars or modals use a slightly lighter brown with a subtle 1px border in a muted gold (`#D4A373` at 15% opacity) to define edges without harsh contrast.

Shadows should be soft and diffused (e.g., `blur: 24px, spread: -4px`), suggesting the objects are gently resting on a surface rather than hovering high above it.

## Shapes

The shape language is **Rounded**, reflecting the soft, organic forms of proofed dough and artisanal loaves. Hard edges are strictly avoided to maintain the "welcoming" brand pillar.

- **Standard Elements:** Buttons and input fields use a 0.5rem radius.
- **Large Containers:** Cards and image containers use a 1rem radius.
- **Decorative Elements:** Occasional use of fully circular "stamps" (e.g., for "Est. 1994" badges) to mimic wax seals or flour dustings.

## Components

### Buttons
Primary buttons are solid Golden Amber with dark charcoal text. Secondary buttons use a "ghost" style with a 1px amber border and no fill. Both utilize a 0.5rem corner radius and a subtle hover transition that increases the "glow" (shadow spread).

### Cards
Cards are used to showcase bakery items or stories. They feature a Dark Chocolate background, soft rounded corners, and high-quality photography. Text within cards should be center-aligned to emphasize the artisanal, menu-like feel.

### Input Fields & Controls
Inputs are minimalist, featuring a dark background slightly deeper than the container they sit in. Borders appear only on focus in a soft amber. Checkboxes and radio buttons use the Golden Amber color for selected states.

### Menus & Lists
Menu items (e.g., the Daily Bread list) should use the Serif headline for the item name and the Sans-serif for descriptions. Use a thin, muted gold divider line (opacity 10%) between list items to maintain structure without cluttering the dark theme.

### Featured Story Component
A specialized component consisting of a full-width image with an overlaid Noto Serif headline. This is used to communicate the bakery's philosophy or heritage, focusing on the "human" element behind the craft.