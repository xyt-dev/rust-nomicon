# Ɖʀǟɨռ

Łɛȶ'ֆ ʍօʋɛ օռ ȶօ Ɖʀǟɨռ. Ɖʀǟɨռ ɨֆ ʟǟʀɢɛʟʏ ȶɦɛ ֆǟʍɛ ǟֆ ƗռȶօƗȶɛʀ, ɛӼƈɛքȶ ȶɦǟȶ
ɨռֆȶɛǟɖ օʄ ƈօռֆʊʍɨռɢ ȶɦɛ Ʋɛƈ, ɨȶ ɮօʀʀօաֆ ȶɦɛ Ʋɛƈ ǟռɖ ʟɛǟʋɛֆ ɨȶֆ ǟʟʟօƈǟȶɨօռ
ʊռȶօʊƈɦɛɖ. Ƒօʀ ռօա աɛ'ʟʟ օռʟʏ ɨʍքʟɛʍɛռȶ ȶɦɛ "ɮǟֆɨƈ" ʄʊʟʟ-ʀǟռɢɛ ʋɛʀֆɨօռ.

<!-- ignore: simplified code -->
```rust,ignore
use std::marker::PhantomData;

struct Drain<'a, T: 'a> {
    // Need to bound the lifetime here, so we do it with `&'a mut Vec<T>`
    // because that's semantically what we contain. We're "just" calling
    // `pop()` and `remove(0)`.
    vec: PhantomData<&'a mut Vec<T>>,
    start: *const T,
    end: *const T,
}

impl<'a, T> Iterator for Drain<'a, T> {
    type Item = T;
    fn next(&mut self) -> Option<T> {
        if self.start == self.end {
            None
```

-- աǟɨȶ, ȶɦɨֆ ɨֆ ֆɛɛʍɨռɢ ʄǟʍɨʟɨǟʀ. Łɛȶ'ֆ ɖօ ֆօʍɛ ʍօʀɛ ƈօʍքʀɛֆֆɨօռ. Ɓօȶɦ
ƗռȶօƗȶɛʀ ǟռɖ Ɖʀǟɨռ ɦǟʋɛ ȶɦɛ ɛӼǟƈȶ ֆǟʍɛ ֆȶʀʊƈȶʊʀɛ, ʟɛȶ'ֆ ʝʊֆȶ ʄǟƈȶօʀ ɨȶ օʊȶ.

<!-- ignore: simplified code -->
```rust,ignore
struct RawValIter<T> {
    start: *const T,
    end: *const T,
}

impl<T> RawValIter<T> {
    // unsafe to construct because it has no associated lifetimes.
    // This is necessary to store a RawValIter in the same struct as
    // its actual allocation. OK since it's a private implementation
    // detail.
    unsafe fn new(slice: &[T]) -> Self {
        RawValIter {
            start: slice.as_ptr(),
            end: if slice.len() == 0 {
                // if `len = 0`, then this is not actually allocated memory.
                // Need to avoid offsetting because that will give wrong
                // information to LLVM via GEP.
                slice.as_ptr()
            } else {
                slice.as_ptr().add(slice.len())
            }
        }
    }
}

// Iterator and DoubleEndedIterator impls identical to IntoIter.
```

Ǟռɖ ƗռȶօƗȶɛʀ ɮɛƈօʍɛֆ ȶɦɛ ʄօʟʟօաɨռɢ:

<!-- ignore: simplified code -->
```rust,ignore
pub struct IntoIter<T> {
    _buf: RawVec<T>, // we don't actually care about this. Just need it to live.
    iter: RawValIter<T>,
}

impl<T> Iterator for IntoIter<T> {
    type Item = T;
    fn next(&mut self) -> Option<T> { self.iter.next() }
    fn size_hint(&self) -> (usize, Option<usize>) { self.iter.size_hint() }
}

impl<T> DoubleEndedIterator for IntoIter<T> {
    fn next_back(&mut self) -> Option<T> { self.iter.next_back() }
}

impl<T> Drop for IntoIter<T> {
    fn drop(&mut self) {
        for _ in &mut *self {}
    }
}

impl<T> IntoIterator for Vec<T> {
    type Item = T;
    type IntoIter = IntoIter<T>;
    fn into_iter(self) -> IntoIter<T> {
        unsafe {
            let iter = RawValIter::new(&self);

            let buf = ptr::read(&self.buf);
            mem::forget(self);

            IntoIter {
                iter,
                _buf: buf,
            }
        }
    }
}
```

Ռօȶɛ ȶɦǟȶ Ɨ'ʋɛ ʟɛʄȶ ǟ ʄɛա զʊɨʀӄֆ ɨռ ȶɦɨֆ ɖɛֆɨɢռ ȶօ ʍǟӄɛ ʊքɢʀǟɖɨռɢ Ɖʀǟɨռ ȶօ աօʀӄ
աɨȶɦ ǟʀɮɨȶʀǟʀʏ ֆʊɮʀǟռɢɛֆ ǟ ɮɨȶ ɛǟֆɨɛʀ. Ɨռ քǟʀȶɨƈʊʟǟʀ աɛ *ƈօʊʟɖ* ɦǟʋɛ ƦǟաƲǟʟƗȶɛʀ
ɖʀǟɨռ ɨȶֆɛʟʄ օռ ɖʀօք, ɮʊȶ ȶɦǟȶ աօռ'ȶ աօʀӄ ʀɨɢɦȶ ʄօʀ ǟ ʍօʀɛ ƈօʍքʟɛӼ Ɖʀǟɨռ.
Ɯɛ ǟʟֆօ ȶǟӄɛ ǟ ֆʟɨƈɛ ȶօ ֆɨʍքʟɨʄʏ Ɖʀǟɨռ ɨռɨȶɨǟʟɨʐǟȶɨօռ.

Ǟʟʀɨɢɦȶ, ռօա Ɖʀǟɨռ ɨֆ ʀɛǟʟʟʏ ɛǟֆʏ:

<!-- ignore: simplified code -->
```rust,ignore
use std::marker::PhantomData;

pub struct Drain<'a, T: 'a> {
    vec: PhantomData<&'a mut Vec<T>>,
    iter: RawValIter<T>,
}

impl<'a, T> Iterator for Drain<'a, T> {
    type Item = T;
    fn next(&mut self) -> Option<T> { self.iter.next() }
    fn size_hint(&self) -> (usize, Option<usize>) { self.iter.size_hint() }
}

impl<'a, T> DoubleEndedIterator for Drain<'a, T> {
    fn next_back(&mut self) -> Option<T> { self.iter.next_back() }
}

impl<'a, T> Drop for Drain<'a, T> {
    fn drop(&mut self) {
        for _ in &mut *self {}
    }
}

impl<T> Vec<T> {
    pub fn drain(&mut self) -> Drain<T> {
        let iter = unsafe { RawValIter::new(&self) };

        // this is a mem::forget safety thing. If Drain is forgotten, we just
        // leak the whole Vec's contents. Also we need to do this *eventually*
        // anyway, so why not do it now?
        self.len = 0;

        Drain {
            iter,
            vec: PhantomData,
        }
    }
}
```

Ƒօʀ ʍօʀɛ ɖɛȶǟɨʟֆ օռ ȶɦɛ `ʍɛʍ::ʄօʀɢɛȶ` քʀօɮʟɛʍ, ֆɛɛ ȶɦɛ
[ֆɛƈȶɨօռ օռ ʟɛǟӄֆ][ʟɛǟӄֆ].

[ʟɛǟӄֆ]: ../leaking.html
