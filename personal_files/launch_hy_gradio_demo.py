import unibox as ub
from tr_core.utils.comfyui_utils import workflow_to_iface

title = "Expert-Guided Multistep t2i Demo"
description = """
用一个低分辨率的composition expert model (p1) 来给sdxl提供更好的构图; 

(应该)不需要quality tag, character应该比较难直接出; artist效果会有所降低; 自然语言效果会比danbooru tag好

sample artists: `jyt, ciloranko, naga_u, nyoijizai, azumi_kazuki, henreader, kantoku, sy4, ningen_mame, ogipote, noeru, ask_\\(askzy\\), ke-ta, velahka, terada_tera, peach11_01, hoji_hooooooooji1029, note_nii, yanyan_\(shinken_gomi\), hamigakikoice`


如果图太窄推荐把浏览器缩放调小; 输入和图的框可以拖选调整尺寸; 结果大概需要20秒

- `api_positive`: prompt; 自然语言效果会比danbooru tag好; 

- `api_seed`: -1是随机, 其他是固定seed

- `Shift + Enter` 可以提交请求
"""


def create_demo():

    wf = ub.loads(
        # "/rmt/yada/dev/training-flow/data/latent_upscale_workflow_api.json"
        "hunyuan_modeldistill_super_API.json"
        )
    iface = workflow_to_iface(wf, 
                              title=title, 
                              description=description, 
                              save_dir = "/rmt/yada/dev/training-flow/data/inference_hunyuan_multistage"
                              )
    iface.api_name = "demo_sdxl_comfy_pag_hires"
    return iface


if __name__ == "__main__":
    demo = create_demo()
    demo.launch(share=True)