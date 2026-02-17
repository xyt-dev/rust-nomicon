# Ƈօɛʀƈɨօռֆ

Ƭʏքɛֆ ƈǟռ ɨʍքʟɨƈɨȶʟʏ ɮɛ ƈօɛʀƈɛɖ ȶօ ƈɦǟռɢɛ ɨռ ƈɛʀȶǟɨռ ƈօռȶɛӼȶֆ.
Ƭɦɛֆɛ ƈɦǟռɢɛֆ ǟʀɛ ɢɛռɛʀǟʟʟʏ ʝʊֆȶ *աɛǟӄɛռɨռɢ* օʄ ȶʏքɛֆ, ʟǟʀɢɛʟʏ ʄօƈʊֆɛɖ ǟʀօʊռɖ քօɨռȶɛʀֆ ǟռɖ ʟɨʄɛȶɨʍɛֆ.
Ƭɦɛʏ ʍօֆȶʟʏ ɛӼɨֆȶ ȶօ ʍǟӄɛ Ʀʊֆȶ "ʝʊֆȶ աօʀӄ" ɨռ ʍօʀɛ ƈǟֆɛֆ, ǟռɖ ǟʀɛ ʟǟʀɢɛʟʏ ɦǟʀʍʟɛֆֆ.

Ƒօʀ ǟռ ɛӼɦǟʊֆȶɨʋɛ ʟɨֆȶ օʄ ǟʟʟ ȶɦɛ ȶʏքɛֆ օʄ ƈօɛʀƈɨօռֆ, ֆɛɛ ȶɦɛ [Ƈօɛʀƈɨօռ ȶʏքɛֆ] ֆɛƈȶɨօռ օռ ȶɦɛ ʀɛʄɛʀɛռƈɛ.

Ռօȶɛ ȶɦǟȶ աɛ ɖօ ռօȶ քɛʀʄօʀʍ ƈօɛʀƈɨօռֆ աɦɛռ ʍǟȶƈɦɨռɢ ȶʀǟɨȶֆ (ɛӼƈɛքȶ ʄօʀ ʀɛƈɛɨʋɛʀֆ, ֆɛɛ ȶɦɛ [ռɛӼȶ քǟɢɛ][ɖօȶ-օքɛʀǟȶօʀ]).
Ɨʄ ȶɦɛʀɛ ɨֆ ǟռ `ɨʍքʟ` ʄօʀ ֆօʍɛ ȶʏքɛ `Ʊ` ǟռɖ `Ƭ` ƈօɛʀƈɛֆ ȶօ `Ʊ`, ȶɦǟȶ ɖօɛֆ ռօȶ ƈօռֆȶɨȶʊȶɛ ǟռ ɨʍքʟɛʍɛռȶǟȶɨօռ ʄօʀ `Ƭ`.
Ƒօʀ ɛӼǟʍքʟɛ, ȶɦɛ ʄօʟʟօաɨռɢ աɨʟʟ ռօȶ ȶʏքɛ ƈɦɛƈӄ, ɛʋɛռ ȶɦօʊɢɦ ɨȶ ɨֆ ØӃ ȶօ ƈօɛʀƈɛ `ȶ` ȶօ `&Ƭ` ǟռɖ ȶɦɛʀɛ ɨֆ ǟռ `ɨʍքʟ` ʄօʀ `&Ƭ`:

```rust,compile_fail
trait Trait {}

fn foo<X: Trait>(t: X) {}

impl<'a> Trait for &'a i32 {}

fn main() {
    let t: &mut i32 = &mut 0;
    foo(t);
}
```

աɦɨƈɦ ʄǟɨʟֆ ʟɨӄɛ ǟֆ ʄօʟʟօաֆ:

```text
error[E0277]: the trait bound `&mut i32: Trait` is not satisfied
 --> src/main.rs:9:9
  |
3 | fn foo<X: Trait>(t: X) {}
  |           ----- required by this bound in `foo`
...
9 |     foo(t);
  |         ^ the trait `Trait` is not implemented for `&mut i32`
  |
  = help: the following implementations were found:
            <&'a i32 as Trait>
  = note: `Trait` is implemented for `&i32`, but not for `&mut i32`
```

[Ƈօɛʀƈɨօռ ȶʏքɛֆ]: https://doc.rust-lang.org/reference/type-coercions.html#coercion-types
[ɖօȶ-օքɛʀǟȶօʀ]: ./dot-operator.html
