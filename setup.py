import setuptools

setuptools.setup(
    name="robloxpy-wrapper",
    version="0.0.1",
    author="Rukchad Wongprayoon",
    author_email="contact@biomooping.tk",
    description="A wrapper for Roblox's API",
    long_description=open('readme.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dumb-stuff/roblox-api-wrapper.git",
    packages=["robloxpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=["requests","aiohttp[speedups]"]
)
