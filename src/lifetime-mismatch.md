# Łɨʍɨȶֆ օʄ Łɨʄɛȶɨʍɛֆ

Ɠɨʋɛռ ȶɦɛ ʄօʟʟօաɨռɢ ƈօɖɛ:

```rust,compile_fail
#[derive(Debug)]
struct Foo;

impl Foo {
    fn mutate_and_share(&mut self) -> &Self { &*self }
    fn share(&self) {}
}

fn main() {
    let mut foo = Foo;
    let loan = foo.mutate_and_share();
    foo.share();
    println!("{:?}", loan);
}
```

Øռɛ ʍɨɢɦȶ ɛӼքɛƈȶ ɨȶ ȶօ ƈօʍքɨʟɛ. Ɯɛ ƈǟʟʟ `ʍʊȶǟȶɛ_ǟռɖ_ֆɦǟʀɛ`, աɦɨƈɦ ʍʊȶǟɮʟʏ
ɮօʀʀօաֆ `ʄօօ` ȶɛʍքօʀǟʀɨʟʏ, ɮʊȶ ȶɦɛռ ʀɛȶʊʀռֆ օռʟʏ ǟ ֆɦǟʀɛɖ ʀɛʄɛʀɛռƈɛ. Ƭɦɛʀɛʄօʀɛ
աɛ աօʊʟɖ ɛӼքɛƈȶ `ʄօօ.ֆɦǟʀɛ()` ȶօ ֆʊƈƈɛɛɖ ǟֆ `ʄօօ` ֆɦօʊʟɖռ'ȶ ɮɛ ʍʊȶǟɮʟʏ ɮօʀʀօաɛɖ.

Ӈօաɛʋɛʀ աɦɛռ աɛ ȶʀʏ ȶօ ƈօʍքɨʟɛ ɨȶ:

```text
error[E0502]: cannot borrow `foo` as immutable because it is also borrowed as mutable
  --> src/main.rs:12:5
   |
11 |     let loan = foo.mutate_and_share();
   |                --- mutable borrow occurs here
12 |     foo.share();
   |     ^^^ immutable borrow occurs here
13 |     println!("{:?}", loan);
```

Ɯɦǟȶ ɦǟքքɛռɛɖ? Ɯɛʟʟ, աɛ ɢօȶ ȶɦɛ ɛӼǟƈȶ ֆǟʍɛ ʀɛǟֆօռɨռɢ ǟֆ աɛ ɖɨɖ ʄօʀ
[ƐӼǟʍքʟɛ 2 ɨռ ȶɦɛ քʀɛʋɨօʊֆ ֆɛƈȶɨօռ][ɛӼ2]. Ɯɛ ɖɛֆʊɢǟʀ ȶɦɛ քʀօɢʀǟʍ ǟռɖ աɛ ɢɛȶ
ȶɦɛ ʄօʟʟօաɨռɢ:

<!-- ignore: desugared code -->
```rust,ignore
struct Foo;

impl Foo {
    fn mutate_and_share<'a>(&'a mut self) -> &'a Self { &'a *self }
    fn share<'a>(&'a self) {}
}

fn main() {
    'b: {
        let mut foo: Foo = Foo;
        'c: {
            let loan: &'c Foo = Foo::mutate_and_share::<'c>(&'c mut foo);
            'd: {
                Foo::share::<'d>(&'d foo);
            }
            println!("{:?}", loan);
        }
    }
}
```

Ƭɦɛ ʟɨʄɛȶɨʍɛ ֆʏֆȶɛʍ ɨֆ ʄօʀƈɛɖ ȶօ ɛӼȶɛռɖ ȶɦɛ `&ʍʊȶ ʄօօ` ȶօ ɦǟʋɛ ʟɨʄɛȶɨʍɛ `'ƈ`,
ɖʊɛ ȶօ ȶɦɛ ʟɨʄɛȶɨʍɛ օʄ `ʟօǟռ` ǟռɖ `ʍʊȶǟȶɛ_ǟռɖ_ֆɦǟʀɛ`'ֆ ֆɨɢռǟȶʊʀɛ. Ƭɦɛռ աɦɛռ աɛ
ȶʀʏ ȶօ ƈǟʟʟ `ֆɦǟʀɛ`, ɨȶ ֆɛɛֆ աɛ'ʀɛ ȶʀʏɨռɢ ȶօ ǟʟɨǟֆ ȶɦǟȶ `&'ƈ ʍʊȶ ʄօօ` ǟռɖ
ɮʟօաֆ ʊք ɨռ օʊʀ ʄǟƈɛ!

Ƭɦɨֆ քʀօɢʀǟʍ ɨֆ ƈʟɛǟʀʟʏ ƈօʀʀɛƈȶ ǟƈƈօʀɖɨռɢ ȶօ ȶɦɛ ʀɛʄɛʀɛռƈɛ ֆɛʍǟռȶɨƈֆ աɛ ǟƈȶʊǟʟʟʏ
ƈǟʀɛ ǟɮօʊȶ, ɮʊȶ ȶɦɛ ʟɨʄɛȶɨʍɛ ֆʏֆȶɛʍ ɨֆ ȶօօ ƈօǟʀֆɛ-ɢʀǟɨռɛɖ ȶօ ɦǟռɖʟɛ ȶɦǟȶ.

## Ɨʍքʀօքɛʀʟʏ ʀɛɖʊƈɛɖ ɮօʀʀօաֆ

Ƭɦɛ ʄօʟʟօաɨռɢ ƈօɖɛ ʄǟɨʟֆ ȶօ ƈօʍքɨʟɛ, ɮɛƈǟʊֆɛ Ʀʊֆȶ ֆɛɛֆ ȶɦǟȶ ǟ ʋǟʀɨǟɮʟɛ, `ʍǟք`,
ɨֆ ɮօʀʀօաɛɖ ȶաɨƈɛ, ǟռɖ ƈǟռ ռօȶ ɨռʄɛʀ ȶɦǟȶ ȶɦɛ ʄɨʀֆȶ ɮօʀʀօա ƈɛǟֆɛֆ ȶօ ɮɛ ռɛɛɖɛɖ
ɮɛʄօʀɛ ȶɦɛ ֆɛƈօռɖ օռɛ օƈƈʊʀֆ. Ƭɦɨֆ ɨֆ ƈǟʊֆɛɖ ɮʏ Ʀʊֆȶ ƈօռֆɛʀʋǟȶɨʋɛʟʏ ʄǟʟʟɨռɢ ɮǟƈӄ
ȶօ ʊֆɨռɢ ǟ աɦօʟɛ ֆƈօքɛ ʄօʀ ȶɦɛ ʄɨʀֆȶ ɮօʀʀօա. Ƭɦɨֆ աɨʟʟ ɛʋɛռȶʊǟʟʟʏ ɢɛȶ ʄɨӼɛɖ.

```rust,compile_fail
# use std::collections::HashMap;
# use std::hash::Hash;
fn get_default<'m, K, V>(map: &'m mut HashMap<K, V>, key: K) -> &'m mut V
where
    K: Clone + Eq + Hash,
    V: Default,
{
    match map.get_mut(&key) {
        Some(value) => value,
        None => {
            map.insert(key.clone(), V::default());
            map.get_mut(&key).unwrap()
        }
    }
}
```

Ɓɛƈǟʊֆɛ օʄ ȶɦɛ ʟɨʄɛȶɨʍɛ ʀɛֆȶʀɨƈȶɨօռֆ ɨʍքօֆɛɖ, `&ʍʊȶ ʍǟք`'ֆ ʟɨʄɛȶɨʍɛ
օʋɛʀʟǟքֆ օȶɦɛʀ ʍʊȶǟɮʟɛ ɮօʀʀօաֆ, ʀɛֆʊʟȶɨռɢ ɨռ ǟ ƈօʍքɨʟɛ ɛʀʀօʀ:

```text
error[E0499]: cannot borrow `*map` as mutable more than once at a time
  --> src/main.rs:12:13
   |
4  |   fn get_default<'m, K, V>(map: &'m mut HashMap<K, V>, key: K) -> &'m mut V
   |                  -- lifetime `'m` defined here
...
9  |       match map.get_mut(&key) {
   |       -     --- first mutable borrow occurs here
   |  _____|
   | |
10 | |         Some(value) => value,
11 | |         None => {
12 | |             map.insert(key.clone(), V::default());
   | |             ^^^ second mutable borrow occurs here
13 | |             map.get_mut(&key).unwrap()
14 | |         }
15 | |     }
   | |_____- returning this value requires that `*map` is borrowed for `'m`
```

[ɛӼ2]: lifetimes.html#example-aliasing-a-mutable-reference
