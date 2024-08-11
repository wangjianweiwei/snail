class ImageUploader {
  constructor(quill, options) {
    this.quill = quill;
    this.options = options;

    // 绑定事件处理器
    this.quill.getModule('toolbar').addHandler('image', this.selectLocalImage.bind(this));
    this.quill.on('text-change', (delta, oldDelta, source) => {
      console.log(1)
      if (source === 'user') {
        console.log(2)
        this.handlePaste(delta);
      }
    });
  }

  selectLocalImage() {
    console.log("selectLocalImage")
    const input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', 'image/*');
    input.click();

    input.onchange = () => {
      const file = input.files[0];

      if (/^image\//.test(file.type)) {
        this.uploadImage(file);
      } else {
        console.warn('You could only upload images.');
      }
    };
  }

  handlePaste(delta) {
    delta.ops.forEach(op => {
      console.log(3)
      if (op.insert?.image) {
        console.log(4)
        const matches = op.insert.image.match(/data:image\/([a-zA-Z]*);base64,([^\"]*)/);

        if (matches && matches[0]) {
          console.log(5)
          this.uploadBase64Image(matches[0]);
        }
      }
    });
  }

  uploadBase64Image(base64Image) {
    console.log(6)
    fetch(`${this.options.uploadUrl}?type=1`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({image: base64Image}),
    })
      .then(response => response.json())
      .then(result => {
        const imageUrl = result.data.url;
        this.replaceBase64ImageWithUrl(base64Image, imageUrl);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  replaceBase64ImageWithUrl(base64Image, imageUrl) {
    const delta = this.quill.getContents();
    delta.ops.forEach((op, index) => {
      if (op.insert && typeof op.insert === 'string' && op.insert.includes(base64Image)) {
        delta.ops[index] = {insert: {image: imageUrl}};
      }
    });

    this.quill.setContents(delta);
  }

  uploadImage(file) {
    const formData = new FormData();
    formData.append('image', file);

    fetch(`${this.options.uploadUrl}?type=2`, {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(result => {
        const imageUrl = result.data.url;
        this.insertToEditor(imageUrl);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  insertToEditor(url) {
    const range = this.quill.getSelection();
    this.quill.insertEmbed(range.index, 'image', url);
  }
}

export {ImageUploader}
