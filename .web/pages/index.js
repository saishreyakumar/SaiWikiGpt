/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Box as RadixThemesBox, Button as RadixThemesButton, Container as RadixThemesContainer, Flex as RadixThemesFlex, Heading as RadixThemesHeading, Slider as RadixThemesSlider, Text as RadixThemesText, TextField as RadixThemesTextField } from "@radix-ui/themes"
import { DebounceInput } from "react-debounce-input"
import { EventLoopContext, StateContexts } from "$/utils/context"
import { Event, isTrue } from "$/utils/state"
import NextHead from "next/head"



export function Debounceinput_1f337025d1eb4d902ffb98ed4fd9f4f5 () {
  
  const reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state = useContext(StateContexts.reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_3bee325d4413cf1988cb2c579af28039 = useCallback(((_e) => (addEvents([(Event("reflex___state____state.sai_wiki_gpt____sai_wiki_gpt____state.set_prompt", ({ ["value"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    <DebounceInput css={({ ["width"] : "100%" })} debounceTimeout={300} element={RadixThemesTextField.Root} onChange={on_change_3bee325d4413cf1988cb2c579af28039} placeholder={"Enter your prompt..."} value={reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state.prompt}/>
  )
}

export function Slider_4f216fc518798d4c3976e1b80cb33cdc () {
  
  const reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state = useContext(StateContexts.reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_62ce562fac1c2ca4ef857c8a4dc3e4ea = useCallback(((_ev_0) => (addEvents([(Event("reflex___state____state.sai_wiki_gpt____sai_wiki_gpt____state.set_max_tokens", ({ ["value"] : _ev_0.at(0) }), ({  })))], [_ev_0], ({  })))), [addEvents, Event])



  
  return (
    <RadixThemesSlider css={({ ["width"] : "100%", ["min"] : 10, ["max"] : 100 })} defaultValue={[50]} onValueChange={on_change_62ce562fac1c2ca4ef857c8a4dc3e4ea} step={10} value={[reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state.max_tokens]} width={"100%"}/>
  )
}

export function Button_7985432001fd332469fc5a63201566cb () {
  
  const reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state = useContext(StateContexts.reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_a353245c9f34778b114b3f8c706e18dc = useCallback(((...args) => (addEvents([(Event("reflex___state____state.sai_wiki_gpt____sai_wiki_gpt____state.generate", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    <RadixThemesButton css={({ ["isLoading"] : reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state.loading })} onClick={on_click_a353245c9f34778b114b3f8c706e18dc}>

{"Generate"}
</RadixThemesButton>
  )
}

export function Text_42bdf7e8140ffb5aa519321bac09f03b () {
  
  const reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state = useContext(StateContexts.reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state)





  
  return (
    <RadixThemesText as={"p"} css={({ ["marginTop"] : "0.5em", ["whiteSpace"] : "pre-wrap" })}>

{reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state.generated_text}
</RadixThemesText>
  )
}

export function Fragment_dda88120484571a7b66e5b7f318b1fa2 () {
  
  const reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state = useContext(StateContexts.reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state)





  
  return (
    <Fragment>

{!((reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state.history === [])) ? (
  <Fragment>

<RadixThemesBox css={({ ["marginTop"] : "1em", ["padding"] : "1em", ["borderRadius"] : "md" })}>

<RadixThemesText as={"p"} css={({ ["fontWeight"] : "bold", ["marginTop"] : "2em" })}>

{"Prompt History:"}
</RadixThemesText>
<>{ reflex___state____state__sai_wiki_gpt____sai_wiki_gpt____state.history.map((item, index_9bc116792391bda4) => (
  <RadixThemesText as={"p"} key={index_9bc116792391bda4}>

{("\ud83d\udcdd "+item.at(0)+" \u2192 "+item.at(1))}
</RadixThemesText>
))}</>
</RadixThemesBox>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Button_a05011703e3d29ad0a560c8f875f7956 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_4d0202f0fc9a511aa0ca8896f1923254 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.sai_wiki_gpt____sai_wiki_gpt____state.regenerate", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    <RadixThemesButton onClick={on_click_4d0202f0fc9a511aa0ca8896f1923254} variant={"outline"}>

{"Regenerate"}
</RadixThemesButton>
  )
}

export default function Component() {
    




  return (
    <Fragment>

<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["height"] : "100vh" })}>

<RadixThemesContainer css={({ ["padding"] : "2em", ["maxWidth"] : "700px" })} size={"3"}>

<RadixThemesHeading size={"4"}>

{" SaiWikiGPT Text Generator"}
</RadixThemesHeading>
<RadixThemesText as={"p"}>

{"Enter a prompt below and generate text."}
</RadixThemesText>
<Debounceinput_1f337025d1eb4d902ffb98ed4fd9f4f5/>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["marginTop"] : "1em" })} direction={"row"} gap={"4"}>

<Button_7985432001fd332469fc5a63201566cb/>
<Button_a05011703e3d29ad0a560c8f875f7956/>
</RadixThemesFlex>
<RadixThemesText as={"p"}>

{"Max Tokens:"}
</RadixThemesText>
<Slider_4f216fc518798d4c3976e1b80cb33cdc/>
<RadixThemesText as={"p"} css={({ ["marginTop"] : "2em", ["fontWeight"] : "bold" })}>

{"Generated Output:"}
</RadixThemesText>
<Text_42bdf7e8140ffb5aa519321bac09f03b/>
<Fragment_dda88120484571a7b66e5b7f318b1fa2/>
</RadixThemesContainer>
</RadixThemesFlex>
<NextHead>

<title>

{"Saiwikigpt | Index"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
