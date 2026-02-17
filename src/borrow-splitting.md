# Ֆքʟɨȶȶɨռɢ Ɓօʀʀօաֆ

Ƭɦɛ ʍʊȶʊǟʟ ɛӼƈʟʊֆɨօռ քʀօքɛʀȶʏ օʄ ʍʊȶǟɮʟɛ ʀɛʄɛʀɛռƈɛֆ ƈǟռ ɮɛ ʋɛʀʏ ʟɨʍɨȶɨռɢ աɦɛռ
աօʀӄɨռɢ աɨȶɦ ǟ ƈօʍքօֆɨȶɛ ֆȶʀʊƈȶʊʀɛ. Ƭɦɛ ɮօʀʀօա ƈɦɛƈӄɛʀ (ǟ.ӄ.ǟ. ɮօʀʀօաƈӄ)
ʊռɖɛʀֆȶǟռɖֆ ֆօʍɛ ɮǟֆɨƈ ֆȶʊʄʄ, ɮʊȶ աɨʟʟ ʄǟʟʟ օʋɛʀ քʀɛȶȶʏ ɛǟֆɨʟʏ. Ɨȶ ɖօɛֆ
ʊռɖɛʀֆȶǟռɖ ֆȶʀʊƈȶֆ ֆʊʄʄɨƈɨɛռȶʟʏ ȶօ ӄռօա ȶɦǟȶ ɨȶ'ֆ քօֆֆɨɮʟɛ ȶօ ɮօʀʀօա ɖɨֆʝօɨռȶ
ʄɨɛʟɖֆ օʄ ǟ ֆȶʀʊƈȶ ֆɨʍʊʟȶǟռɛօʊֆʟʏ. Ֆօ ȶɦɨֆ աօʀӄֆ ȶօɖǟʏ:

```rust
struct Foo {
    a: i32,
    b: i32,
    c: i32,
}

let mut x = Foo {a: 0, b: 0, c: 0};
let a = &mut x.a;
let b = &mut x.b;
let c = &x.c;
*b += 1;
let c2 = &x.c;
*a += 10;
println!("{} {} {} {}", a, b, c, c2);
```

Ӈօաɛʋɛʀ ɮօʀʀօաƈӄ ɖօɛֆռ'ȶ ʊռɖɛʀֆȶǟռɖ ǟʀʀǟʏֆ օʀ ֆʟɨƈɛֆ ɨռ ǟռʏ աǟʏ, ֆօ ȶɦɨֆ ɖօɛֆռ'ȶ
աօʀӄ:

```rust,compile_fail
let mut x = [1, 2, 3];
let a = &mut x[0];
let b = &mut x[1];
println!("{} {}", a, b);
```

```text
error[E0499]: cannot borrow `x[..]` as mutable more than once at a time
 --> src/lib.rs:4:18
  |
3 |     let a = &mut x[0];
  |                  ---- first mutable borrow occurs here
4 |     let b = &mut x[1];
  |                  ^^^^ second mutable borrow occurs here
5 |     println!("{} {}", a, b);
6 | }
  | - first borrow ends here

error: aborting due to previous error
```

Ɯɦɨʟɛ ɨȶ աǟֆ քʟǟʊֆɨɮʟɛ ȶɦǟȶ ɮօʀʀօաƈӄ ƈօʊʟɖ ʊռɖɛʀֆȶǟռɖ ȶɦɨֆ ֆɨʍքʟɛ ƈǟֆɛ, ɨȶ'ֆ
քʀɛȶȶʏ ƈʟɛǟʀʟʏ ɦօքɛʟɛֆֆ ʄօʀ ɮօʀʀօաƈӄ ȶօ ʊռɖɛʀֆȶǟռɖ ɖɨֆʝօɨռȶռɛֆֆ ɨռ ɢɛռɛʀǟʟ
ƈօռȶǟɨռɛʀ ȶʏքɛֆ ʟɨӄɛ ǟ ȶʀɛɛ, ɛֆքɛƈɨǟʟʟʏ ɨʄ ɖɨֆȶɨռƈȶ ӄɛʏֆ ǟƈȶʊǟʟʟʏ *ɖօ* ʍǟք
ȶօ ȶɦɛ ֆǟʍɛ ʋǟʟʊɛ.

Ɨռ օʀɖɛʀ ȶօ "ȶɛǟƈɦ" ɮօʀʀօաƈӄ ȶɦǟȶ աɦǟȶ աɛ'ʀɛ ɖօɨռɢ ɨֆ օӄ, աɛ ռɛɛɖ ȶօ ɖʀօք ɖօառ
ȶօ ʊռֆǟʄɛ ƈօɖɛ. Ƒօʀ ɨռֆȶǟռƈɛ, ʍʊȶǟɮʟɛ ֆʟɨƈɛֆ ɛӼքօֆɛ ǟ `ֆքʟɨȶ_ǟȶ_ʍʊȶ` ʄʊռƈȶɨօռ
ȶɦǟȶ ƈօռֆʊʍɛֆ ȶɦɛ ֆʟɨƈɛ ǟռɖ ʀɛȶʊʀռֆ ȶաօ ʍʊȶǟɮʟɛ ֆʟɨƈɛֆ. Øռɛ ʄօʀ ɛʋɛʀʏȶɦɨռɢ ȶօ
ȶɦɛ ʟɛʄȶ օʄ ȶɦɛ ɨռɖɛӼ, ǟռɖ օռɛ ʄօʀ ɛʋɛʀʏȶɦɨռɢ ȶօ ȶɦɛ ʀɨɢɦȶ. Ɨռȶʊɨȶɨʋɛʟʏ աɛ ӄռօա
ȶɦɨֆ ɨֆ ֆǟʄɛ ɮɛƈǟʊֆɛ ȶɦɛ ֆʟɨƈɛֆ ɖօռ'ȶ օʋɛʀʟǟք, ǟռɖ ȶɦɛʀɛʄօʀɛ ǟʟɨǟֆ. Ӈօաɛʋɛʀ
ȶɦɛ ɨʍքʟɛʍɛռȶǟȶɨօռ ʀɛզʊɨʀɛֆ ֆօʍɛ ʊռֆǟʄɛȶʏ:

```rust
# use std::slice::from_raw_parts_mut;
# struct FakeSlice<T>(T);
# impl<T> FakeSlice<T> {
# fn len(&self) -> usize { unimplemented!() }
# fn as_mut_ptr(&mut self) -> *mut T { unimplemented!() }
pub fn split_at_mut(&mut self, mid: usize) -> (&mut [T], &mut [T]) {
    let len = self.len();
    let ptr = self.as_mut_ptr();

    unsafe {
        assert!(mid <= len);

        (from_raw_parts_mut(ptr, mid),
         from_raw_parts_mut(ptr.add(mid), len - mid))
    }
}
# }
```

Ƭɦɨֆ ɨֆ ǟƈȶʊǟʟʟʏ ǟ ɮɨȶ ֆʊɮȶʟɛ. Ֆօ ǟֆ ȶօ ǟʋօɨɖ ɛʋɛʀ ʍǟӄɨռɢ ȶաօ `&ʍʊȶ`'ֆ ȶօ ȶɦɛ
ֆǟʍɛ ʋǟʟʊɛ, աɛ ɛӼքʟɨƈɨȶʟʏ ƈօռֆȶʀʊƈȶ ɮʀǟռɖ-ռɛա ֆʟɨƈɛֆ ȶɦʀօʊɢɦ ʀǟա քօɨռȶɛʀֆ.

Ӈօաɛʋɛʀ ʍօʀɛ ֆʊɮȶʟɛ ɨֆ ɦօա ɨȶɛʀǟȶօʀֆ ȶɦǟȶ ʏɨɛʟɖ ʍʊȶǟɮʟɛ ʀɛʄɛʀɛռƈɛֆ աօʀӄ.
Ƭɦɛ ɨȶɛʀǟȶօʀ ȶʀǟɨȶ ɨֆ ɖɛʄɨռɛɖ ǟֆ ʄօʟʟօաֆ:

```rust
trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

Ɠɨʋɛռ ȶɦɨֆ ɖɛʄɨռɨȶɨօռ, Ֆɛʟʄ::Ɨȶɛʍ ɦǟֆ *ռօ* ƈօռռɛƈȶɨօռ ȶօ `ֆɛʟʄ`. Ƭɦɨֆ ʍɛǟռֆ ȶɦǟȶ
աɛ ƈǟռ ƈǟʟʟ `ռɛӼȶ` ֆɛʋɛʀǟʟ ȶɨʍɛֆ ɨռ ǟ ʀօա, ǟռɖ ɦօʟɖ օռȶօ ǟʟʟ ȶɦɛ ʀɛֆʊʟȶֆ
*ƈօռƈʊʀʀɛռȶʟʏ*. Ƭɦɨֆ ɨֆ քɛʀʄɛƈȶʟʏ ʄɨռɛ ʄօʀ ɮʏ-ʋǟʟʊɛ ɨȶɛʀǟȶօʀֆ, աɦɨƈɦ ɦǟʋɛ
ɛӼǟƈȶʟʏ ȶɦɛֆɛ ֆɛʍǟռȶɨƈֆ. Ɨȶ'ֆ ǟʟֆօ ǟƈȶʊǟʟʟʏ ʄɨռɛ ʄօʀ ֆɦǟʀɛɖ ʀɛʄɛʀɛռƈɛֆ, ǟֆ ȶɦɛʏ
ǟɖʍɨȶ ǟʀɮɨȶʀǟʀɨʟʏ ʍǟռʏ ʀɛʄɛʀɛռƈɛֆ ȶօ ȶɦɛ ֆǟʍɛ ȶɦɨռɢ (ǟʟȶɦօʊɢɦ ȶɦɛ ɨȶɛʀǟȶօʀ ռɛɛɖֆ
ȶօ ɮɛ ǟ ֆɛքǟʀǟȶɛ օɮʝɛƈȶ ʄʀօʍ ȶɦɛ ȶɦɨռɢ ɮɛɨռɢ ֆɦǟʀɛɖ).

Ɓʊȶ ʍʊȶǟɮʟɛ ʀɛʄɛʀɛռƈɛֆ ʍǟӄɛ ȶɦɨֆ ǟ ʍɛֆֆ. Ǟȶ ʄɨʀֆȶ ɢʟǟռƈɛ, ȶɦɛʏ ʍɨɢɦȶ ֆɛɛʍ
ƈօʍքʟɛȶɛʟʏ ɨռƈօʍքǟȶɨɮʟɛ աɨȶɦ ȶɦɨֆ ǞՔƗ, ǟֆ ɨȶ աօʊʟɖ քʀօɖʊƈɛ ʍʊʟȶɨքʟɛ ʍʊȶǟɮʟɛ
ʀɛʄɛʀɛռƈɛֆ ȶօ ȶɦɛ ֆǟʍɛ օɮʝɛƈȶ!

Ӈօաɛʋɛʀ ɨȶ ǟƈȶʊǟʟʟʏ *ɖօɛֆ* աօʀӄ, ɛӼǟƈȶʟʏ ɮɛƈǟʊֆɛ ɨȶɛʀǟȶօʀֆ ǟʀɛ օռɛ-ֆɦօȶ օɮʝɛƈȶֆ.
Ɛʋɛʀʏȶɦɨռɢ ǟռ ƗȶɛʀⱮʊȶ ʏɨɛʟɖֆ աɨʟʟ ɮɛ ʏɨɛʟɖɛɖ ǟȶ ʍօֆȶ օռƈɛ, ֆօ աɛ ɖօռ'ȶ
ǟƈȶʊǟʟʟʏ ɛʋɛʀ ʏɨɛʟɖ ʍʊʟȶɨքʟɛ ʍʊȶǟɮʟɛ ʀɛʄɛʀɛռƈɛֆ ȶօ ȶɦɛ ֆǟʍɛ քɨɛƈɛ օʄ ɖǟȶǟ.

Քɛʀɦǟքֆ ֆʊʀքʀɨֆɨռɢʟʏ, ʍʊȶǟɮʟɛ ɨȶɛʀǟȶօʀֆ ɖօռ'ȶ ʀɛզʊɨʀɛ ʊռֆǟʄɛ ƈօɖɛ ȶօ ɮɛ
ɨʍքʟɛʍɛռȶɛɖ ʄօʀ ʍǟռʏ ȶʏքɛֆ!

Ƒօʀ ɨռֆȶǟռƈɛ ɦɛʀɛ'ֆ ǟ ֆɨռɢʟʏ ʟɨռӄɛɖ ʟɨֆȶ:

```rust
# fn main() {}
type Link<T> = Option<Box<Node<T>>>;

struct Node<T> {
    elem: T,
    next: Link<T>,
}

pub struct LinkedList<T> {
    head: Link<T>,
}

pub struct IterMut<'a, T: 'a>(Option<&'a mut Node<T>>);

impl<T> LinkedList<T> {
    fn iter_mut(&mut self) -> IterMut<T> {
        IterMut(self.head.as_mut().map(|node| &mut **node))
    }
}

impl<'a, T> Iterator for IterMut<'a, T> {
    type Item = &'a mut T;

    fn next(&mut self) -> Option<Self::Item> {
        self.0.take().map(|node| {
            self.0 = node.next.as_mut().map(|node| &mut **node);
            &mut node.elem
        })
    }
}
```

Ӈɛʀɛ'ֆ ǟ ʍʊȶǟɮʟɛ ֆʟɨƈɛ:

```rust
# fn main() {}
use std::mem;

pub struct IterMut<'a, T: 'a>(&'a mut[T]);

impl<'a, T> Iterator for IterMut<'a, T> {
    type Item = &'a mut T;

    fn next(&mut self) -> Option<Self::Item> {
        let slice = mem::take(&mut self.0);
        if slice.is_empty() { return None; }

        let (l, r) = slice.split_at_mut(1);
        self.0 = r;
        l.get_mut(0)
    }
}

impl<'a, T> DoubleEndedIterator for IterMut<'a, T> {
    fn next_back(&mut self) -> Option<Self::Item> {
        let slice = mem::take(&mut self.0);
        if slice.is_empty() { return None; }

        let new_len = slice.len() - 1;
        let (l, r) = slice.split_at_mut(new_len);
        self.0 = l;
        r.get_mut(0)
    }
}
```

Ǟռɖ ɦɛʀɛ'ֆ ǟ ɮɨռǟʀʏ ȶʀɛɛ:

```rust
# fn main() {}
use std::collections::VecDeque;

type Link<T> = Option<Box<Node<T>>>;

struct Node<T> {
    elem: T,
    left: Link<T>,
    right: Link<T>,
}

pub struct Tree<T> {
    root: Link<T>,
}

struct NodeIterMut<'a, T: 'a> {
    elem: Option<&'a mut T>,
    left: Option<&'a mut Node<T>>,
    right: Option<&'a mut Node<T>>,
}

enum State<'a, T: 'a> {
    Elem(&'a mut T),
    Node(&'a mut Node<T>),
}

pub struct IterMut<'a, T: 'a>(VecDeque<NodeIterMut<'a, T>>);

impl<T> Tree<T> {
    pub fn iter_mut(&mut self) -> IterMut<T> {
        let mut deque = VecDeque::new();
        if let Some(root) = self.root.as_mut() {
            deque.push_front(root.iter_mut());
        }
        IterMut(deque)
    }
}

impl<T> Node<T> {
    pub fn iter_mut(&mut self) -> NodeIterMut<T> {
        NodeIterMut {
            elem: Some(&mut self.elem),
            left: self.left.as_deref_mut(),
            right: self.right.as_deref_mut(),
        }
    }
}

impl<'a, T> Iterator for NodeIterMut<'a, T> {
    type Item = State<'a, T>;

    fn next(&mut self) -> Option<Self::Item> {
        self.left.take().map(State::Node).or_else(|| {
            self.elem
                .take()
                .map(State::Elem)
                .or_else(|| self.right.take().map(State::Node))
        })
    }
}

impl<'a, T> DoubleEndedIterator for NodeIterMut<'a, T> {
    fn next_back(&mut self) -> Option<Self::Item> {
        self.right.take().map(State::Node).or_else(|| {
            self.elem
                .take()
                .map(State::Elem)
                .or_else(|| self.left.take().map(State::Node))
        })
    }
}

impl<'a, T> Iterator for IterMut<'a, T> {
    type Item = &'a mut T;
    fn next(&mut self) -> Option<Self::Item> {
        loop {
            match self.0.front_mut().and_then(Iterator::next) {
                Some(State::Elem(elem)) => return Some(elem),
                Some(State::Node(node)) => self.0.push_front(node.iter_mut()),
                None => {
                    self.0.pop_front()?;
                }
            }
        }
    }
}

impl<'a, T> DoubleEndedIterator for IterMut<'a, T> {
    fn next_back(&mut self) -> Option<Self::Item> {
        loop {
            match self.0.back_mut().and_then(DoubleEndedIterator::next_back) {
                Some(State::Elem(elem)) => return Some(elem),
                Some(State::Node(node)) => self.0.push_back(node.iter_mut()),
                None => {
                    self.0.pop_back()?;
                }
            }
        }
    }
}
```

Ǟʟʟ օʄ ȶɦɛֆɛ ǟʀɛ ƈօʍքʟɛȶɛʟʏ ֆǟʄɛ ǟռɖ աօʀӄ օռ ֆȶǟɮʟɛ Ʀʊֆȶ! Ƭɦɨֆ ʊʟȶɨʍǟȶɛʟʏ
ʄǟʟʟֆ օʊȶ օʄ ȶɦɛ ֆɨʍքʟɛ ֆȶʀʊƈȶ ƈǟֆɛ աɛ ֆǟա ɮɛʄօʀɛ: Ʀʊֆȶ ʊռɖɛʀֆȶǟռɖֆ ȶɦǟȶ ʏօʊ
ƈǟռ ֆǟʄɛʟʏ ֆքʟɨȶ ǟ ʍʊȶǟɮʟɛ ʀɛʄɛʀɛռƈɛ ɨռȶօ ֆʊɮʄɨɛʟɖֆ. Ɯɛ ƈǟռ ȶɦɛռ ɛռƈօɖɛ
քɛʀʍǟռɛռȶʟʏ ƈօռֆʊʍɨռɢ ǟ ʀɛʄɛʀɛռƈɛ ʋɨǟ Øքȶɨօռֆ (օʀ ɨռ ȶɦɛ ƈǟֆɛ օʄ ֆʟɨƈɛֆ,
ʀɛքʟǟƈɨռɢ աɨȶɦ ǟռ ɛʍքȶʏ ֆʟɨƈɛ).
